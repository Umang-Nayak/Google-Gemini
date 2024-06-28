import os
import google.generativeai as genai
from prompts import prompt1, prompt2, prompt3
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


chat = model.start_chat()


token_per_given_price = 1000000
flash_15_input = 0.35
flash_15_output = 1.05
pro_15_input = 3.50
pro_15_output = 10.50
pro_10_input = 0.50
pro_10_output = 1.50

input_token = []
output_token = []

prompt = prompt3

while True:
    question = input("\nMe : \n")
    if question.lower() == "stop":
        if not prompt:
            print("-------------------------------------------------")
            print(f"Input Token = {sum(input_token)}")
            print(f"Output Token = {sum(output_token)}")
            print(f"Total Request = {len(output_token)}")
            print("-------------------------------------------------")

            input_price_flash_15 = (sum(input_token) * flash_15_input) / token_per_given_price
            output_price_flash_15 = (sum(output_token) * flash_15_output) / token_per_given_price
            print(f"Price for Flash 1.5 = {input_price_flash_15 + output_price_flash_15}")

            input_price_pro_15 = (sum(input_token) * pro_15_input) / token_per_given_price
            output_price_pro_15 = (sum(output_token) * pro_15_output) / token_per_given_price
            price_pro_15 = input_price_pro_15 + output_price_pro_15
            print(f"Price for Pro 1.5 = {price_pro_15}")

            input_price_pro_10 = (sum(input_token) * pro_10_input) / token_per_given_price
            output_price_pro_10 = (sum(output_token) * pro_10_output) / token_per_given_price
            price_pro_10 = input_price_pro_10 + output_price_pro_10
            print(f"Price for Pro 1.0 = {price_pro_10}")

        else:
            print("-------------------------------------------------")
            print(f"Input Token = {sum(input_token) + (len(prompt) * len(input_token))}")
            print(f"Output Token = {sum(output_token)}")
            print(f"Total Request = {len(output_token)}")
            print("-------------------------------------------------")

            input_price_flash_15 = ((sum(input_token) + (len(prompt) * len(input_token))) * flash_15_input) / token_per_given_price
            output_price_flash_15 = (sum(output_token) * flash_15_output) / token_per_given_price
            print(f"Price for Flash 1.5 = {input_price_flash_15 + output_price_flash_15}")

            input_price_pro_15 = ((sum(input_token) + (len(prompt) * len(input_token))) * pro_15_input) / token_per_given_price
            output_price_pro_15 = (sum(output_token) * pro_15_output) / token_per_given_price
            price_pro_15 = input_price_pro_15 + output_price_pro_15
            print(f"Price for Pro 1.5 = {price_pro_15}")

            input_price_pro_10 = ((sum(input_token) + (len(prompt) * len(input_token))) * pro_10_input) / token_per_given_price
            output_price_pro_10 = (sum(output_token) * pro_10_output) / token_per_given_price
            price_pro_10 = input_price_pro_10 + output_price_pro_10
            print(f"Price for Pro 1.0 = {price_pro_10}")
        break
    else:
        response = chat.send_message([prompt3, question])
        # print(response)
        input_token.append(model.count_tokens(question).total_tokens)
        print("\nGemini : \n", response.text)
        output_token.append(model.count_tokens(response.text).total_tokens)
