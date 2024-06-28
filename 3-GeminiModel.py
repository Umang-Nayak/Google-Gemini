import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

print("All Gemini Model Name :")

# Get All Gemini Model Name
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
