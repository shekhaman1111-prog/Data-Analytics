import os
from google import genai

# Reads GEMINI_API_KEY from your environment
client = genai.Client(api_key=os.getenv("AQ.Ab8RN6KZDOwwh4YQJQXW7DLHnhbbV3Ti9AlsifMYcD6Lpectmw"))

def aiProcess(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are Jarvis, a helpful AI assistant. "
                "Give short and concise answers.\n\n"
                f"User: {command}"
            )
        )

        return response.text or "I couldn't generate a response."

    except Exception as e:
        print("Gemini API Error:", e)
        return "I am having trouble connecting to the AI server."