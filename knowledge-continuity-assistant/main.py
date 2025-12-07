import streamlit as st
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
import random

from config import EMBEDDING_MODEL, CHAT_MODEL
from agents.pipeline_agent import run_pipeline
from agents.retriever_agent import get_retriever
from agents.csv_agent import load_job_dataset
from agents.reader_agent import reader_agent

# ✅ Setup halaman
st.set_page_config(page_title="Knowledge Continuity Assistant", page_icon="🤖", layout="wide")

# 🌱 Load environment
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# 🧠 Init session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "persona" not in st.session_state:
    st.session_state.persona = "(Netral)"

# 🧾 Placeholder acak
placeholder_examples = [
    "Laporan weekly apa aja sih yang harus diisi?",
    "Apa aja yang perlu disiapkan buat laporan Imprest Fund?",
    "Siapa yang handle proses settlement mitra sekarang?",
    "Cara rekap revenue bulanan gimana ya?",
    "Proses approval dokumen di Centra kayak gimana?"
]
chat_placeholder = f"Tanya sesuatu kayak: '{random.choice(placeholder_examples)}'"

# 📄 Load dokumen
pdf_paths = ["data/Buku_Panduan_Tim_Support.pdf"]
csv_paths = ["data/dataset_1.csv", "data/dataset_2.csv"]
job_dfs = [load_job_dataset(p) for p in csv_paths if os.path.exists(p)]

# 🔍 Init retriever
try:
    get_retriever(API_KEY)
except:
    try:
        reader_agent(pdf_paths, API_KEY)
        get_retriever(API_KEY)
    except:
        pass

# ========== SIDEBAR ==========
with st.sidebar:
    st.button(
        "➕ New Chat",
        key="new_chat_btn",
        use_container_width=True,
        disabled=not st.session_state.chat_started,
        on_click=lambda: st.session_state.update({
            "conversation_history": [],
            "chat_started": False
        })
    )

    st.markdown("### 💬 Histori Chat")
    if st.session_state.conversation_history:
        for idx, (q, *_rest) in enumerate(st.session_state.conversation_history):
            st.markdown(f"- {q[:40]}")

    st.markdown("### 🎭 Simulasi Jawaban")
    st.session_state.persona = st.selectbox(
        "Pilih persona:",
        ["(Netral)", "Mbak Disa", "Bang Simon", "Mas Arif"],
        key="persona_selector"
    )
    st.caption("🧠 Persona menyesuaikan gaya balasan seperti eks-talent.")

# ========== MAIN AREA ==========
st.title("📌 KNOWLEDGE CONTINUITY ASSISTANT 🤖")

# 💬 Chat Riwayat
if st.session_state.conversation_history:
    for q, a, model, time, source, persona in st.session_state.conversation_history:
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(q)
        with st.chat_message("assistant", avatar="🤖"):
            if persona != "(Netral)":
                st.markdown(f"*🧠 Dijawab sebagai {persona}*")
            st.markdown(a)
else:
    st.markdown("📭 **Belum ada pertanyaan. Coba mulai bertanya di bawah!**")

# ℹ️ Footer
st.markdown("---")
st.caption("📘 Dokumen referensi: Buku Panduan Team Support Tribe IOT Platform & Services")

# 📥 Chat Input (masuk ke session_state)
user_input = st.chat_input(chat_placeholder)

# Saat user kirim → simpan input ke state dan tandai untuk diproses
if user_input:
    st.session_state.user_input = user_input
    st.session_state.run_now = True
    st.rerun()

# Proses pertanyaan jika ada flag
if st.session_state.get("run_now", False):
    with st.spinner("🔍 Memproses pertanyaan..."):
        # Real pipeline
        output_text, source_name = run_pipeline(
            st.session_state.user_input,
            API_KEY,
            job_dfs,
            st.session_state.persona
        )

    # ✅ Simpan ke histori
    st.session_state.conversation_history.append((
        st.session_state.user_input,
        output_text,
        "Google AI",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        source_name,
        st.session_state.persona
    ))
    st.session_state.chat_started = True

    # ✅ Tampilkan langsung jawaban terbaru sebelum rerun
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(st.session_state.user_input)

    with st.chat_message("assistant", avatar="🤖"):
        if st.session_state.persona != "(Netral)":
            st.markdown(f"*🧠 Dijawab sebagai {st.session_state.persona}*")
        st.markdown(output_text)

    # 🚫 Hapus flag dan rerun
    del st.session_state.run_now
    del st.session_state.user_input
    st.rerun()
