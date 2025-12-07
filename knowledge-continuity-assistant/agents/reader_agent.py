from utils.pdf_utils import extract_text_from_pdf, get_text_chunks
from utils.vector_utils import create_vectorstore
from config import EMBEDDING_MODEL

def split_pdf_into_chunks(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    chunks = get_text_chunks(text)
    return chunks

def reader_agent(pdf_paths, api_key):
    all_chunks = []
    for path in pdf_paths:
        chunks = split_pdf_into_chunks(path)
        all_chunks.extend(chunks)

    vectorstore = create_vectorstore(all_chunks, api_key)
    return vectorstore
