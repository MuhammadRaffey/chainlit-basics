import chainlit as cl
from dotenv import load_dotenv
import os
from mistralai import Mistral

load_dotenv()

# Debug logging
api_key = os.getenv("MISTRAL_API_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")
print(f"API Key length: {len(api_key) if api_key else 0}")

@cl.on_message
async def handle_message(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    mistral = Mistral(api_key=api_key)
    
    stream_response = mistral.chat.stream(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": message.content}],
    )

    for chunk in stream_response:
        if chunk.data.choices[0].delta.content:
            await msg.stream_token(chunk.data.choices[0].delta.content)

