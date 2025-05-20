# File: backend/main.py
import fitz  # PyMuPDF

def get_pdf_chunks(pdf_path, max_chars=1000):
    doc = fitz.open(pdf_path)
    chunks = []
    text = ""
    for page in doc:
        text += page.get_text()
    # Split text into smaller chunks
    for i in range(0, len(text), max_chars):
        chunk = text[i:i+max_chars].strip()
        if chunk:
            chunks.append(chunk)
    return chunks

def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5
    return dot_product / (norm_a * norm_b + 1e-8)  # small epsilon to avoid zero division
