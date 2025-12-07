from agents.retriever_agent import retrieve_chunks
from agents.csv_agent import search_job_info_from_multiple_datasets
from agents.answer_agent import answer_question

def hybrid_agent(question: str, api_key: str, job_dfs=None, persona_instruction: str = "") -> str:
    """
    Gabungkan konteks dari PDF dan CSV lalu jawab pakai LLM, sesuai gaya persona jika diberikan.
    """
    # 1. PDF Context
    pdf_chunks = retrieve_chunks(question, api_key)
    pdf_context = "\n\n".join(pdf_chunks) if pdf_chunks else ""

    # 2. CSV Context
    csv_context = search_job_info_from_multiple_datasets(question, job_dfs) if job_dfs else ""

    # 3. Gabungkan kedua konteks
    combined_context = f"{pdf_context}\n\n{csv_context}".strip()
    if not combined_context:
        combined_context = "Tidak ada konteks relevan dari PDF maupun CSV."

    # 4. Jawab pertanyaan dengan instruksi persona (jika ada)
    return answer_question(question, combined_context, api_key, persona=persona_instruction)
