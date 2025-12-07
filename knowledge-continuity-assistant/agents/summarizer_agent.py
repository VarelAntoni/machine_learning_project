from langchain_google_genai import ChatGoogleGenerativeAI

def summarizer_agent(context_docs, api_key):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=api_key)

    content = "\n\n".join([doc.page_content for doc in context_docs])
    prompt = f"""
Berikan ringkasan singkat dan jelas dari isi berikut:

{content}

🔍 RINGKASAN:
"""

    return model.invoke(prompt)
