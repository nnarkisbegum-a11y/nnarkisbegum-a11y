import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"