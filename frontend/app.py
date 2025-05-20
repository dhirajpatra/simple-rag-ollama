# File: backend/main.py
import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("📄 PDF-based RAG Chatbot")

query = st.text_input("Ask a question based on your PDFs:")

if st.button("Submit") and query.strip():
    with st.spinner("Getting answer..."):
        response = requests.get("http://backend:8000/query/", params={"query": query})
        if response.status_code == 200:
            st.markdown("### 💬 Response")
            st.write(response.json()["response"])
        else:
            st.error("Something went wrong. Please try again.")
