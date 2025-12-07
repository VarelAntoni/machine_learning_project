import argparse
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.reader_agent import reader_agent

def main(pdf_paths, api_key):
    if not api_key:
        print("❌ API key Google belum diberikan. Gunakan argumen --api_key.")
        return

    for path in pdf_paths:
        if not os.path.exists(path):
            print(f"❌ File tidak ditemukan: {path}")
            return

    print("📦 Membuat FAISS vectorstore dari PDF...")
    reader_agent(pdf_paths, api_key)
    print("✅ Index FAISS berhasil dibuat dan disimpan ke direktori 'faiss_index'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index PDF ke FAISS untuk chatbot retrieval.")
    parser.add_argument("--pdfs", nargs="+", required=True, help="Daftar path ke file PDF")
    parser.add_argument("--api_key", type=str, required=True, help="Google API Key")
    args = parser.parse_args()

    main(args.pdfs, args.api_key)
