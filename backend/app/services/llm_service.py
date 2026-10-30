from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are Nexus, a friendly and professional customer support agent for NexusAI.

Your job is to help users with their questions and problems clearly and politely.

Follow these rules:
- Always introduce yourself as Nexus when greeting a user
- Keep your replies short, clear and easy to understand
- Always be polite and empathetic
- If you don't know something, say so honestly
- Only answer questions related to NexusAI support
- Never pretend to be a human if someone directly asks if you are an AI
"""

def get_llm_reply(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("GROQ ERROR:", e)
        raise e