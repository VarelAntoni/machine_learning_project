import requests

# API Key langsung didefinisikan di sini
EXA_API_KEY = "5d373967-051c-4777-b03d-a230a1ef4ae3"

def search_web(query: str, max_results: int = 3) -> str:
    """
    Fallback ke Exa.ai sebagai semantic search engine.
    """
    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {EXA_API_KEY}"
        }

        payload = {
            "query": query,
            "num_results": max_results
        }

        response = requests.post("https://api.exa.ai/search", headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])
        if not results:
            return "❗ Tidak ditemukan informasi relevan dari Exa.ai."

        output = ""
        for i, r in enumerate(results):
            title = r.get("title", "Tanpa judul")
            snippet = r.get("text", "")
            url = r.get("url", "")
            output += f"**{i+1}. {title}**\n{snippet}\n🔗 {url}\n\n"

        return output.strip()

    except Exception as e:
        return f"❌ Gagal mengambil data dari Exa.ai: {str(e)}"
