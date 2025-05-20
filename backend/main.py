# backend/main.py
import os
os.environ['OLLAMA_API_URL'] = os.getenv('OLLAMA_API_URL', 'http://ollama:11434')
import ollama
from fastapi import FastAPI, UploadFile
from rag_engine import process_query, ingest_pdfs

app = FastAPI()

@app.on_event("startup")
def load_documents():
    ingest_pdfs("documents")

@app.get("/")
def read_root():
    return {"message": "RAG Backend is running."}

@app.get("/query/")
def query_knowledge(query: str):
    response = process_query(query)
    return {"response": response}
