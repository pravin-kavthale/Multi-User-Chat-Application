import asyncio
from django.conf import settings
from google.genai import Client

client = Client(api_key=settings.GENAI_API_KEY) 

async def get_bot_response(user_message: str) -> str:
    """
    Sends the user_message to Gemini API and returns the response.
    """
    return await asyncio.to_thread(
        lambda: client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=user_message,
            config={"temperature": 0.7} 
        ).text 
    )