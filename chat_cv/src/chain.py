from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_qa_chain():
    # 1. Ambil Tanggal Hari Ini (Agar AI tahu "Sekarang" itu kapan)
    current_date = datetime.now().strftime("%B %Y")  # Contoh: "December 2025"
    linkedin_url = os.getenv("LINKEDIN_URL", "LinkedIn Saya")

    # 2. Prompt Engineering yang Lebih Cerdas
    prompt_template = f"""
    Kamu adalah Asisten AI Profesional dan Personal Recruiter untuk VAREL yang sedang melamar sebagai DATA SCIENTIST.
    
    KONTEKS WAKTU: Hari ini adalah {current_date}.
    
    TUGAS UTAMA:
    Jawab pertanyaan user berdasarkan konteks CV yang diberikan dengan fokus MENJUAL kompetensi teknis Varel.

    ATURAN PRIORITAS (PENTING!!!):
    1. **HIERARKI PENGALAMAN:**
       - Jika user bertanya tentang "Pengalaman", "Experience", atau "Kerja":
       - **WAJIB UTAMAKAN** Pengalaman Kerja Profesional (Internship, Project-Based, Full-time) di urutan paling atas.
       - Contoh Profesional: CADIT Consultants, Telkom Indonesia, Home Credit, DBS Coding Camp.
       - **NOMORDUAKAN** Pengalaman Organisasi/Kepanitiaan (Society of Renewable Energy, Manager, Staff, dsb). Taruh ini di bagian paling bawah atau hanya jika relevan dengan soft skill.

    2. **URUTAN WAKTU:**
       - Di dalam kategori Profesional, urutkan dari yang TERBARU (Present/2025) ke yang LAMA.
    
    3. **GAYA BAHASA:**
       - Gunakan poin-poin (bullet points) agar mudah dibaca.
       - Sertakan durasi waktu di setiap pengalaman.
       - Jangan hanya menyalin jobdesk, tapi **highlight tools** (Python, YOLO, RAG, SQL) yang dipakai di pengalaman tersebut.

    Context (Isi CV):
    {{context}}
    
    Pertanyaan User: 
    {{question}}
    
    Jawaban (Fokus Profesional):
    """
    
    # Gunakan model yang sudah terbukti bekerja di akun Anda
    model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.3)
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)