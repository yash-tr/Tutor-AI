import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.get_model("models/text-bison-001")

def get_ai_tutor_response(query: str) -> str:
    try:
        response = model.generate_text(prompt=query)
        return response.result
    except Exception as e:
        return f"Error: {str(e)}"
