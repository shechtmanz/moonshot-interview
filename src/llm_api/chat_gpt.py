from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os

class ChatGpt:
    _GPT_MODEL = "gpt-3.5-turbo"

    def __init__(self):
        load_dotenv()
        open_ai_key = os.getenv("OPENAI_API_KEY")
        if not open_ai_key:
            raise Exception ("Environment variable OPENAI_API_KEYa is not defined")
        
        self._open_ai_client = OpenAI(api_key=open_ai_key)
        self._messages = [ {"role": "system", "content": "You are a legal expert."} ]

    def ask_chat(self, prompt: str) -> str:
        self._messages.append({"role": "user", "content": prompt})
        response = self._open_ai_client.chat.completions.create( model=ChatGpt._GPT_MODEL, messages=self._messages) 
        reply_message = response.choices[0].message.content 
        self._messages.append({"role": "assistant", "content": reply_message})     
        return reply_message