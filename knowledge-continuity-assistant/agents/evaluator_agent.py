from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from config import CHAT_MODEL

EVALUATOR_PROMPT = PromptTemplate(
    input_variables=["question", "context", "answer"],
    template="""
Kamu adalah evaluator jawaban AI untuk asisten internal perusahaan.

Berikut ini adalah:
❓ Pertanyaan pengguna:
{question}

📄 Konteks dokumen:
{context}

🤖 Jawaban AI:
{answer}

Tugasmu adalah mengevaluasi apakah jawaban sudah benar, lengkap, dan sesuai konteks.

Buat penilaian ringkas dengan format seperti ini:
- Relevansi: [Ya/Tidak]
- Kelengkapan: [Lengkap/Cukup/Tidak Lengkap]
- Feedback: [komentar evaluator]

Jawab dalam Bahasa Indonesia.
"""
)

def evaluate_answer(question: str, context: str, answer: str, api_key: str) -> str:
    """
    Mengevaluasi apakah jawaban sudah relevan dan lengkap terhadap pertanyaan dan konteks.
    """
    prompt = EVALUATOR_PROMPT.format(question=question, context=context, answer=answer)
    llm = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0.3, google_api_key=api_key)
    return llm.invoke(prompt)
