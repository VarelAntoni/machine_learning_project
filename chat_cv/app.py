import streamlit as st
import os
import csv
from datetime import datetime
from dotenv import load_dotenv
from src import utils, vectorstore, chain

# Load Env
load_dotenv()

# --- FUNGSI BARU: SIMPAN FEEDBACK KE CSV ---
def save_feedback(prompt, response, rating):
    """
    Menyimpan data pertanyaan, jawaban, dan rating user ke file CSV.
    Ini mensimulasikan proses pengumpulan data untuk RLHF (Reinforcement Learning from Human Feedback).
    """
    file_name = 'feedback_log.csv'
    file_exists = os.path.isfile(file_name)
    
    try:
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Tulis header jika file baru dibuat
            if not file_exists:
                writer.writerow(['Timestamp', 'User Prompt', 'Bot Response', 'Rating'])
            
            # Tulis data baru
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, response, rating])
            
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan feedback: {e}")
        return False

# Fungsi pembantu untuk memproses pertanyaan
def handle_user_input(prompt):
    # 1. Tampilkan pertanyaan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Proses jawaban bot
    try:
        db = vectorstore.load_vector_store()
        docs = db.similarity_search(prompt, k=10) 
        qa_chain = chain.get_qa_chain()
        
        response = qa_chain(
            {"input_documents": docs, "question": prompt},
            return_only_outputs=True
        )
        answer = response["output_text"]
        
        # 3. Tampilkan jawaban bot
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

        # --- UPDATE PENTING: SIMPAN STATE UNTUK FEEDBACK ---
        # Kita simpan interaksi terakhir agar bisa dinilai oleh user
        st.session_state.last_interaction = {"prompt": prompt, "response": answer}
        
    except Exception as e:
        st.error(f"Terjadi Error pada AI: {e}")
        st.warning("Tips: Pastikan tombol 'Muat Ulang CV' di sidebar sudah diklik.")

def main():
    st.set_page_config("Get to Know Varel", page_icon="📄", layout="wide")
    st.title("Get to Know About Varel's Experience")
    st.markdown("---")

    # --- SIDEBAR (ADMIN AREA) ---
    with st.sidebar:
        st.subheader("Panel Admin")
        st.info("CV dibaca otomatis dari folder 'data/'")
        
        if st.button("🔄 Muat Ulang / Update CV", type="primary"):
            with st.spinner("Membaca & Mempelajari CV..."):
                try:
                    raw_text = utils.load_pdfs_from_folder("data")
                    if not raw_text:
                        st.error("Tidak ada file PDF ditemukan di folder 'data'!")
                    else:
                        chunks = utils.split_text(raw_text)
                        vectorstore.create_vector_store(chunks)
                        st.success("Ingatan AI berhasil diperbarui!")
                except Exception as e:
                    st.error(f"Terjadi Error: {e}")

        st.markdown("---")
        with st.expander("🔍 Intip Isi Teks PDF"):
             if os.path.exists("data"):
                 try:
                    raw_debug = utils.load_pdfs_from_folder("data")
                    st.text(raw_debug[:2000] + "...") 
                 except:
                    st.text("Gagal membaca file.")
             else:
                 st.write("Folder data belum ada.")

    # --- INIT SESSION STATE ---
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Halo! Saya asisten virtual Varel. Silakan pilih pertanyaan di bawah atau ketik sendiri ya! 👋"
        })
    
    # Inisialisasi state untuk feedback
    if "last_interaction" not in st.session_state:
        st.session_state.last_interaction = None

    # --- BAGIAN 1: SUGGESTION CHIPS ---
    st.subheader("Pertanyaan Cepat:")
    col1, col2, col3, col4 = st.columns(4)
    button_prompt = None

    if col1.button("📋 Ringkasan Profil", use_container_width=True):
        button_prompt = "Berikan ringkasan profil profesional Varel secara singkat dan padat."
    if col2.button("💼 Pengalaman Kerja", use_container_width=True):
        button_prompt = "Jelaskan pengalaman kerja Varel secara urut dari yang terbaru beserta durasinya."
    if col3.button("🛠️ Skill Teknis", use_container_width=True):
        button_prompt = "Apa saja hard skill, bahasa pemrograman, dan tools yang dikuasai Varel?"
    if col4.button("📞 Kontak", use_container_width=True):
        button_prompt = "Bagaimana cara menghubungi Varel? (Email/LinkedIn)"

    # --- BAGIAN 2: HISTORY CHAT ---
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- FITUR BARU: FEEDBACK SECTION (MUNCUL SETELAH JAWABAN) ---
    # Jika ada interaksi terakhir, tampilkan tombol feedback
    if st.session_state.last_interaction:
        st.markdown("---")
        st.caption("🤖 Bantu tingkatkan kecerdasan bot ini:")
        
        col_f1, col_f2, col_f3 = st.columns([1, 1, 5])
        
        with col_f1:
            if st.button("👍 Bagus"):
                last = st.session_state.last_interaction
                if save_feedback(last['prompt'], last['response'], "Positive"):
                    st.toast("Terima kasih atas feedback positifnya!", icon="✅")
                    # Reset state agar tombol hilang setelah diklik (opsional)
                    st.session_state.last_interaction = None
                    st.rerun()

        with col_f2:
            if st.button("👎 Kurang"):
                last = st.session_state.last_interaction
                if save_feedback(last['prompt'], last['response'], "Negative"):
                    st.toast("Terima kasih! Kami akan perbaiki.", icon="📝")
                    st.session_state.last_interaction = None
                    st.rerun()

    # --- BAGIAN 3: INPUT USER ---
    if input_manual := st.chat_input("Tanya sesuatu tentang Varel..."):
        handle_user_input(input_manual)
        st.rerun() # Rerun agar tombol feedback muncul di bawah
    
    elif button_prompt:
        handle_user_input(button_prompt)
        st.rerun()

if __name__ == "__main__":
    main()