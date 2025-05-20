# 🧠 Simple RAG-based PDF Chatbot (FastAPI + Streamlit + Ollama)

This project is a simple Retrieval-Augmented Generation (RAG) chatbot using:

- **FastAPI** as the backend
- **Streamlit** as the frontend
- **Ollama** for embedding and chat models
- **User PDFs** stored in `documents/` folder for context

---

## 📂 Folder Structure

```

.
├── backend/
│   ├── main.py
│   ├── rag\_engine.py
│   ├── utils.py
│   ├── requirements.txt
├── frontend/
│   ├── app.py
│   ├── requirements.txt
├── documents/                  # Place all PDFs here
├── docker-compose.yml
├── entrypoint.sh              # Used in ollama service
└── README.md

````

---

## 📦 Models Used

- Embedding Model: `hf.co/CompendiumLabs/bge-base-en-v1.5-gguf`
- Language Model: `hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF`

These are automatically pulled by the `ollama` container via `entrypoint.sh`.

---

## 🚀 How to Run

### 1. Place your PDFs

Put all your PDF files into the `documents/` folder.

### 2. Start the Application

```bash
./start.sh
````

---

## 🌐 Usage

* Go to `http://localhost:8501`
* Ask questions based on your uploaded PDFs
* Backend uses RAG (embedding + cosine similarity + LLM) to generate answers

---

## 🐋 Services

* **Ollama**: Loads models and performs embedding + chat
* **Backend (FastAPI)**: Handles query and performs retrieval + generation
* **Frontend (Streamlit)**: Simple UI to ask questions

---

## 📝 License

MIT
