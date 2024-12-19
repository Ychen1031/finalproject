import os
import google.generativeai as generativeai
from dotenv import load_dotenv

load_dotenv()
generativeai.configure(api_key= os.getenv('GENERATIVEAIAPI'))
response = generativeai.GenerativeModel('gemini-2.0-flash-exp').generate_content('你是誰')
print(response.text)