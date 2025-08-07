
# RAG-Based Question Answering API using FastAPI, LangChain, FAISS & OpenAI

This project builds a **Retrieval-Augmented Generation (RAG)** system that takes a question in Bengali and returns an answer based on the content of a provided PDF file.

It uses:
- **FastAPI** to build the web API.
- **LangChain** for chaining the document retriever and LLM.
- **FAISS** for vector-based document search.
- **OpenAI GPT** (via API key) for generating answers.
- **PyMuPDF** or `fitz` to load PDF.
- **Uvicorn** as the ASGI server.

---

## 🚀 How It Works

1. Loads and chunks the PDF document.
2. Converts text chunks into vector embeddings using OpenAI.
3. Stores and searches the vectors using FAISS.
4. Answers user questions based on the most relevant text chunks.

---

## 📁 Project Structure
rag_basic/
│
├── app.py # FastAPI app with /query endpoint
├── main.py # LangChain logic for QA over PDF
├── data/ # Folder to store your PDF files
│ └── your_file.pdf # PDF to be queried
├── requirements.txt # List of dependencies
└── README.md # Project overview and instructions

