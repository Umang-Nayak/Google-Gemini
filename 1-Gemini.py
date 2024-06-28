import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

question = input("\nQUESTION = \n")

response = model.generate_content(question)

print("\nANSWER =")
print(response.text)
