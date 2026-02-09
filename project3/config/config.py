import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

if not GEMINI_API_KEY or not SERP_API_KEY:
    raise ValueError("API keys not found. Check your .env file ")
