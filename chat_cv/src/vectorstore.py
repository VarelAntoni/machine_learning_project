# src/vectorstore.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(text_chunks):
    # GANTI 'models/embedding-001' MENJADI 'models/text-embedding-004'
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def load_vector_store():
    # GANTI JUGA DISINI
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)