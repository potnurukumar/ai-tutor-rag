from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables (.env for local development)
load_dotenv()

# Get API key from .env (local) or Streamlit Secrets (cloud)
from src.config import GEMINI_API_KEY

api_key = GEMINI_API_KEY


if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in .env or Streamlit Secrets.")

# Create Gemini client
client = genai.Client(api_key=api_key)


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