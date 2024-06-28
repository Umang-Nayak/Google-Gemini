import os
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open('Images/car-2.jpg')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(img)

print(response.text)
