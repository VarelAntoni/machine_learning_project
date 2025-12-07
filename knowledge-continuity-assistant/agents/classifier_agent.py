from langchain_google_genai import ChatGoogleGenerativeAI

def classify_question(question, api_key):
    """
    Klasifikasi pertanyaan: pdf, csv, both, or none.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        google_api_key=api_key
    )

    prompt = f"""
Tugas kamu adalah mengklasifikasikan pertanyaan berikut menjadi salah satu kategori:
- "pdf": jika isi pertanyaan tentang prosedur, kebijakan, panduan
- "csv": jika berkaitan dengan pekerjaan, teknologi, posisi, lokasi
- "both": jika memerlukan dua sumber tersebut
- "none": jika tidak relevan

Berikan **satu kata jawaban saja** tanpa penjelasan.

Pertanyaan: "{question}"
"""

    try:
        result = llm.invoke(prompt)

        # 🔍 Pastikan result adalah string
        if hasattr(result, "content"):
            response_text = result.content
        else:
            response_text = str(result)

        print("[Classifier Result]:", repr(response_text))
        return response_text.strip().lower()

    except Exception as e:
        print("❌ Classifier Error:", e)
        return "none"
