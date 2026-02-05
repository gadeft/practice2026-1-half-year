from google import genai
from dotenv import load_dotenv


load_dotenv()


def ask_ai(question):
    client = genai.Client(api_key="AIzaSyAycilux_BV1hy-3_lPQKQGx1hKcE6uUXc")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question,
    )

    return response