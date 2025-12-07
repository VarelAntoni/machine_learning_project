import re

def extract_main_topic(question: str) -> str:
    """
    Ambil kata kunci/topik utama dari pertanyaan untuk digunakan dalam pencarian Wikipedia.
    Jika gagal, fallback ke seluruh pertanyaan (diformat).
    """
    # Contoh simple regex untuk ambil noun phrase atau keyword penting
    keywords = re.findall(r'\b(machine learning|python|data science|artificial intelligence|deep learning|tools?)\b', question.lower())
    return keywords[0] if keywords else question.lower().strip().replace(" ", "_")
