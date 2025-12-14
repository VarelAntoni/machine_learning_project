import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("--- DAFTAR MODEL YANG TERSEDIA UNTUK ANDA ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")