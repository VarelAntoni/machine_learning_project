def format_llm_response(response) -> str:
    """
    Mengekstrak isi teks dari response LLM secara aman dan rapi.
    Hapus metadata jika ada, dan pastikan output selalu string bersih.
    """
    if hasattr(response, "text") and callable(response.text):
        result = response.text()
    elif hasattr(response, "content"):
        result = response.content
    elif isinstance(response, str):
        result = response
    else:
        result = str(response)

    # Hilangkan bagian metadata LLM jika ada
    if "response_metadata" in result:
        result = result.split("response_metadata")[0].strip()

    return result.strip()
