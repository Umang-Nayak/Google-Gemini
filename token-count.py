import os
import google.generativeai as genai
from prompts import prompt1, prompt2, prompt3
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')


chat = model.start_chat()

total_input_token = 0
total_output_token = 0


prompt = prompt3

while True:
    question = input("\nMe : \n")
    if question.lower() == "stop":
        print(f"Input Tokens = {total_input_token}")
        print(f"Output Tokens = {total_output_token}")
        break
    else:
        prompt_token = int(model.count_tokens(prompt).total_tokens)
        question_token = int(model.count_tokens(question).total_tokens)
        input_token = prompt_token + question_token

        total_input_token = total_input_token + input_token

        response = chat.send_message([prompt, question])

        answer_token = int(model.count_tokens(response.text).total_tokens)
        total_output_token = total_output_token + answer_token

        print("\nGemini : \n", response.text)
