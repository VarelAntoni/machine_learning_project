# src/utils.py
import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdfs_from_folder(folder_path):
    text = ""
    # Cek apakah folder ada
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' tidak ditemukan.")

    # Loop semua file di folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            pdf_reader = PdfReader(file_path)
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text()
    return text

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=200
    )
    return text_splitter.split_text(text)