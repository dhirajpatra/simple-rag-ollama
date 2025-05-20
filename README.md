# 🧠 Simple RAG-based PDF Chatbot (FastAPI + Streamlit + Ollama)

This project is a simple Retrieval-Augmented Generation (RAG) chatbot using:

- **FastAPI** as the backend
- **Streamlit** as the frontend
- **Ollama** for embedding and chat models
- **User PDFs** stored in `documents/` folder for context

[![Local RAG Chatbot](/images/1.png)]
---

## 📂 Folder Structure

```

├── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── __pycache__  [error opening dir]
│   ├── rag_engine.py
│   ├── requirements.txt
│   └── utils.py
├── docker-compose.yml
├── documents  [error opening dir]
├── entrypoint.sh  [error opening dir]
├── frontend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── ollama
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── id_ed25519
│   ├── ollama_server.py
│   └── requirements.txt
├── README.md
└── start.sh


````

---

## 📦 Models Used

- Embedding Model: `hf.co/CompendiumLabs/bge-base-en-v1.5-gguf`
- Language Model: `hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF`

These are automatically pulled by the `ollama` container via `entrypoint.sh`.

---

## 🚀 How to Run

### 1. Place your PDFs

Put your PDF file(s) into the `documents/` folder. 

### 2. Start the Application

```bash
./start.sh
````

### First time it can take from 10 min to hour depends on your internet speed, system power and number of pdf. To stop the application (all services) run `ctrl + c` in terminal. 

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
