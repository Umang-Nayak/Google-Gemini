import os
import google.generativeai as genai
from prompts import prompt1, prompt2, prompt3
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

question = input("Question : ")
chat = model.generate_content([prompt1, question])
print(chat.text)
