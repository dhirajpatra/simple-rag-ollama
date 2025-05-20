# File: backend/main.py
import os
os.environ['OLLAMA_API_URL'] = os.getenv('OLLAMA_API_URL', 'http://ollama:11434')
import ollama
import fitz  # PyMuPDF
import os
from utils import get_pdf_chunks, cosine_similarity

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

VECTOR_DB = []

def embed_text(text):
    return ollama.embed(model=EMBEDDING_MODEL, input=text)['embeddings'][0]

def add_chunk_to_database(chunk):
    embedding = embed_text(chunk)
    VECTOR_DB.append((chunk, embedding))

def ingest_pdfs(folder_path='documents'):
    # Ingest PDFs only once if VECTOR_DB is empty
    if VECTOR_DB:
        return
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            chunks = get_pdf_chunks(file_path)
            for chunk in chunks:
                add_chunk_to_database(chunk)

def retrieve(query, top_n=3):
    query_embedding = embed_text(query)
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

def process_query(user_input):
    # Ensure PDFs ingested before query processing
    ingest_pdfs()

    retrieved_knowledge = retrieve(user_input)
    instruction_prompt = (
        "You are a helpful chatbot.\n"
        "Use only the following pieces of context to answer the question. "
        "Don't make up any new information:\n"
        + '\n'.join([f" - {chunk}" for chunk, _ in retrieved_knowledge])
    )

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": user_input}
        ],
        stream=True
    )

    response = ""
    for chunk in stream:
        response += chunk['message']['content']
    return response
