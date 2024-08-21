import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("AI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com",
)


def ai_assistant(system_content, role_content):
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": f"You are an editor at a newspaper, {system_content}.",
            },
            {"role": "user", "content": f"{role_content}"},
        ],
    )
    return response.choices[0].message.content
