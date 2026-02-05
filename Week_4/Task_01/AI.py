from google import genai
from dotenv import load_dotenv


load_dotenv()

def ask_ai(question):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question,
    )

    return response