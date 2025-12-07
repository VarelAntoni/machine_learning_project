from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from config import CHAT_MODEL

ANSWER_PROMPT = PromptTemplate(
    input_variables=["question", "context", "history", "persona"],
    template="""
Kamu adalah asisten internal perusahaan yang menjawab berdasarkan dokumen atau data internal.

🎭 Gaya komunikasi yang harus digunakan:
{persona}

Berikut riwayat percakapan sebelumnya (jika ada):
{history}

📄 Informasi/konteks dokumen:
{context}

❓ Pertanyaan pengguna:
{question}

Jawablah dengan bahasa yang ringkas, jelas, dan profesional sesuai gaya di atas.
Jawaban harus berdasarkan konteks, dan tidak boleh mengarang bebas.
Jika tidak tahu jawabannya, katakan sejujurnya bahwa tidak ditemukan dalam data internal.
"""
)

def answer_question(question: str, context: str, api_key: str, history=None, persona: str = "") -> str:
    """
    Jawab pertanyaan berdasarkan context dan gaya komunikasi persona (jika ada).
    """
    if not history:
        history = []
    history_text = "\n\n".join([f"Q: {q}\nA: {a}" for q, a, *_ in history[-3:]])  # max 3 prev pairs

    prompt = ANSWER_PROMPT.format(
        question=question,
        context=context or "Tidak ada konteks eksplisit.",
        history=history_text or "Tidak ada.",
        persona=persona or "Tidak ada preferensi gaya khusus."
    )

    llm = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0.3, google_api_key=api_key)
    return llm.invoke(prompt)
