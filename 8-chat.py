import os
import google.generativeai as genai
from prompts import prompt1, prompt2, prompt3
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')


chat = model.start_chat()

while True:
    question = input("\nMe : \n")
    if question.lower() == "stop":
        break
    else:
        response = chat.send_message([question])
        print("\nGemini : \n", response.text)
