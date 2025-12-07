from langchain_google_genai import ChatGoogleGenerativeAI

def verifier_agent(question, answer, context_docs, api_key):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=api_key)

    context = "\n\n".join([doc.page_content for doc in context_docs])
    prompt = f"""
Tugas Anda adalah mengevaluasi apakah jawaban berikut relevan dan akurat terhadap konteks yang diberikan.

📄 KONTEKS DOKUMEN:
{context}

❓ PERTANYAAN:
{question}

💬 JAWABAN:
{answer}

🔎 EVALUASI:
Tuliskan apakah jawaban sudah sesuai. Jika tidak, beri saran koreksi.
"""

    return model.invoke(prompt)
