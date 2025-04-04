import os
from openai import OpenAI

from dotenv import load_dotenv

from models.booking import Booking
load_dotenv()

class ChatService:
  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
  )

  def chat(self, prompt: str) -> str:
    completion = self.client.chat.completions.create(
      model='gpt-4o',
      messages=[
        {
          'role': 'system',
          'content': 'You are a helpful AI assistant to draw charts'
        },
        {
          'role': 'user',
          'content': prompt
        }
      ]
    )

    return completion.choices[0].message.content
