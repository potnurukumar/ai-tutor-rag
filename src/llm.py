from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_answer(context, question):
    """
    Generate an answer using the retrieved document context.
    """

    if not context.strip():
        return "I couldn't find any relevant information in the uploaded documents."

    prompt = f"""
You are an expert AI Tutor.

Your job is to teach students using ONLY the provided context.

Instructions:
- Answer ONLY from the context below.
- Do NOT use outside knowledge.
- If the answer is not found in the context, reply exactly:
  "I couldn't find this information in the uploaded document."
- Explain the concept in simple language.
- Include:
  • Short definition
  • Simple explanation
  • Example (if available)
- Format the answer using bullet points when appropriate.

==========================
CONTEXT
==========================
{context}

==========================
QUESTION
==========================
{question}

==========================
ANSWER
==========================
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"