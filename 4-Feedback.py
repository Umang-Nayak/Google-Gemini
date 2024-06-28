import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

question = input("\nQUESTION = \n")

response = model.generate_content(question, stream=True)

print("\nFEEDBACK =")
print(response.prompt_feedback)

print("\nANSWER =")
for chunk in response:
    print(chunk.text)



