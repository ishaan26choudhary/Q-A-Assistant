# Q-A-Assistant

A local Question–Answering assistant that answers user queries **strictly from a provided PDF document** using **LangChain**, **Ollama**, and a **local LLM (Mistral)**.

The system follows a Retrieval-Augmented Generation (RAG) pipeline and avoids hallucination when the answer is not present in the document.

---

## Features

- PDF ingestion and text chunking
- Vector-based semantic search
- Local LLM inference using Ollama (no API keys required)
- Clear fallback when the answer is **not present in the PDF**
- Fully offline after model download

---

## Tech Stack

- Python 3.9+
- LangChain
- Ollama
- Mistral LLM
- FAISS (vector store)
- PyPDFLoader

---

## Project Structure

