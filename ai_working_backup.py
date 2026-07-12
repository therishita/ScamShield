import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_text(text):

    prompt = f"""
You are ScamShield, an AI scam detection assistant.

Analyze this message:

{text}

Give:

1. Risk Level (Low / Medium / High)
2. Scam probability
3. Warning signs
4. Explanation
5. Safety advice
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Text analysis failed.\n\n{str(e)}"



def analyze_image(uploaded_file):

    return """
Image analysis is currently under development.

Please use text analysis for the MVP.
"""