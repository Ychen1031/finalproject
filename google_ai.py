import os

import google.generativeai as genai

api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

tak = input('input: ')
response = genai.GenerativeModel('gemini-2.0-flash-exp').generate_content(tak)

print(response.text)