from agents.classifier_agent import classify_question
from agents.qa_agent import qa_agent
from agents.hybrid_agent import hybrid_agent
from agents.answer_agent import answer_question
from agents.csv_agent import search_job_info_from_multiple_datasets
from agents.retriever_agent import retrieve_chunks
from agents.web_search_agent import search_web
from utils.llm_utils import format_llm_response

import streamlit as st

def run_pipeline(question: str, api_key: str, job_dfs=None, persona: str = None) -> tuple[str, str]:
    st.write("▶️ Menjalankan pipeline untuk pertanyaan:", question)

    source = classify_question(question, api_key)
    st.write("🔎 Source diklasifikasi sebagai:", source)

    valid_sources = ["csv", "pdf", "both"]
    if source not in valid_sources:
        st.warning(f"❗ Source tidak dikenali: '{source}', fallback ke 'pdf'")
        source = "pdf"

    history = st.session_state.get("conversation_history", [])

    context = None
    response = None
    source_name = None
    output_text = ""
    internet_answer_text = ""

    # 🔧 Persona style
    persona_prompts = {
        "Mbak Disa": "Jawablah dengan gaya yang ramah, suportif, dan penuh empati seolah kamu adalah Mbak Disa.",
        "Bang Simon": "Gunakan bahasa yang langsung ke inti, santai, dan percaya diri seperti Bang Simon.",
        "Mas Arif": "Gunakan bahasa teknis, jelas, dan sistematis seperti Mas Arif.",
    }
    persona_instruction = persona_prompts.get(persona, "") if persona and persona != "(Netral)" else ""

    # 🔍 Internal first
    if source == "csv":
        context = search_job_info_from_multiple_datasets(question, job_dfs)
        response = answer_question(question, context, api_key, history=history, persona=persona_instruction)
        source_name = "Dataset CSV"

    elif source == "pdf":
        chunks = retrieve_chunks(question, api_key)
        context = "\n\n".join(chunks)
        response = answer_question(question, context, api_key, history=history, persona=persona_instruction)
        source_name = "Dokumen PDF"

    elif source == "both":
        response = hybrid_agent(question, api_key, job_dfs, persona_instruction)
        context = None
        source_name = "Gabungan PDF & Dataset"

    # ✨ Format internal jawaban
    if response:
        internal_answer_text = format_llm_response(response)
        output_text = internal_answer_text
    else:
        output_text = "❌ Maaf, saya tidak menemukan jawaban yang sesuai untuk pertanyaan ini."

    # 🌐 Tambahkan Exa.ai sebagai pelengkap (bukan fallback)
    try:
        internet_answer_text = search_web(question)
        if "❌" not in internet_answer_text and "tidak ditemukan" not in internet_answer_text.lower():
            output_text += "\n\n---\n🌐 *Informasi tambahan dari Exa.ai:*\n"
            output_text += internet_answer_text.strip()
            source_name = f"{source_name} + Exa.ai"
    except Exception as e:
        st.warning(f"Gagal mengambil data dari Exa.ai: {e}")

    st.write("✅ Pipeline selesai. Sumber:", source_name)
    return output_text.strip(), source_name or "Tidak diketahui"
