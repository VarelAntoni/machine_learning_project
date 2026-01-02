# 🧠 Knowledge Continuity Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![RAG](https://img.shields.io/badge/Technique-RAG-orange)

## 📋 Overview

**Knowledge Continuity Assistant** is an intelligent RAG-based (Retrieval-Augmented Generation) chatbot designed to streamline knowledge retrieval within organizations. 

In many companies, valuable information is trapped in static documents (PDFs, DOCX, TXT), leading to knowledge loss when employees leave or transition roles. This tool solves that problem by allowing users to upload internal documents and chat with them using natural language, ensuring critical knowledge remains accessible and interactive.

This project was originally developed as part of a Data Science Internship initiative (e.g., at Telkom Indonesia) to improve internal decision-making processes.

## ✨ Key Features

* **📄 Multi-Document Support:** Upload and process multiple PDF, TXT, or DOCX files simultaneously.
* **🔍 RAG Architecture:** Utilizes vector embeddings to retrieve the most relevant context from documents before generating answers.
* **💬 Interactive Chat Interface:** Built with Streamlit for a user-friendly, chat-like experience.
* **🧠 LLM Integration:** Powered by Large Language Models (e.g., OpenAI GPT / Gemini / Llama) for accurate and context-aware responses.
* **📚 Source Citing:** (Optional) Displays the source documents used to generate the answer to ensure transparency.

## 🛠️ Tech Stack

* **Language:** Python
* **UI Framework:** Streamlit
* **LLM Framework:** LangChain / LlamaIndex
* **Embeddings:** OpenAI Embeddings / HuggingFace Embeddings
* **Vector Database:** FAISS / ChromaDB / Pinecone
* **PDF Processing:** PyPDF2 / LangChain Document Loaders
