from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import EMBEDDING_MODEL

def get_retriever(api_key, index_path="faiss_index"):
    """
    Memuat FAISS vectorstore dan mengembalikan retriever.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=api_key)
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()

def retrieve_chunks(question, api_key, k=5):
    """
    Mengambil potongan dokumen paling relevan terhadap pertanyaan.
    """
    retriever = get_retriever(api_key)
    results = retriever.get_relevant_documents(question, k=k)
    return [doc.page_content for doc in results]
