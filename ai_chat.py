import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(report):
    try:
        response = model.generate_content(report)
        return response.text
    except Exception as e:
        return str(e)