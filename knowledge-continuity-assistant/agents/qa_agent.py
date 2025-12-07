# agents/qa_agent.py

from agents.retriever_agent import retrieve_chunks
from agents.answer_agent import answer_question

def qa_agent(question, api_key):
    """
    QA agent untuk pertanyaan berbasis dokumen PDF internal.
    Mengambil konteks dari retriever dan menjawab via LLM.
    """
    chunks = retrieve_chunks(question, api_key)
    context = "\n\n".join(chunks) if chunks else "Tidak ada konteks relevan ditemukan dari PDF."
    return answer_question(question, context, api_key)
