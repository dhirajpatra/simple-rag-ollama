# File: backend/main.py

import os
import fitz  # PyMuPDF
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_community.llms import Ollama
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from utils import get_pdf_chunks, cosine_similarity

# Set base URL for Ollama from environment variable
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://ollama:11434')

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

# LangChain LLM and embedding clients
llm = Ollama(
    model=LANGUAGE_MODEL,
    base_url=OLLAMA_API_URL,
    temperature=0
)

embedding_client = OllamaEmbeddings(
    model=EMBEDDING_MODEL,
    base_url=OLLAMA_API_URL
)

VECTOR_DB = []

def embed_text(text):
    return embedding_client.embed_query(text)

def add_chunk_to_database(chunk):
    embedding = embed_text(chunk)
    VECTOR_DB.append((chunk, embedding))

def ingest_pdfs(folder_path='documents'):
    if VECTOR_DB:
        print("[INFO] VECTOR_DB already populated.")
        return
    for filename in os.listdir(folder_path):
        print(f"[DEBUG] Processing file: {filename}")
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"[INFO] Ingesting: {file_path}")
            chunks = get_pdf_chunks(file_path)
            for chunk in chunks:
                print(f"[DEBUG] Adding chunk: {chunk[:80]}...")
                add_chunk_to_database(chunk)

def retrieve(query, top_n=3):
    query_embedding = embed_text(query)
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    print(f"[INFO] Top {top_n} matches for query '{query}':")
    for chunk, score in similarities[:top_n]:
        print(f"  [SCORE: {score:.4f}] {chunk[:100]}")
    
    return similarities[:top_n]

def process_query(user_input):
    ingest_pdfs()

    retrieved_knowledge = retrieve(user_input)
    context = '\n'.join([f" - {chunk}" for chunk, _ in retrieved_knowledge])

    prompt = (
        "You are a helpful chatbot.\n"
        "Use only the following pieces of context to answer the question. "
        "Don't make up any new information:\n"
        f"{context}\n\nQuestion: {user_input}"
    )

    return llm.invoke(prompt)

