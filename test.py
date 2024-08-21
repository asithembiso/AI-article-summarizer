from openai import OpenAI

client = OpenAI(
    api_key="52315c5f9b284afcb9cef9e139d4dc5e",
    base_url="https://api.aimlapi.com",
)


def ai_assistant(content):
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an editor ata newspaper.",
            },
            {
                "role": "user",
                "content": f"{content}"
            },
        ],
    )
    return response.choices[0].message.content


message = ai_assistant("Why is the sky blue?")
print(f"Assistant: {message}")
