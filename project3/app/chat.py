
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def chat_with_memory(user_input):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    return response.text
