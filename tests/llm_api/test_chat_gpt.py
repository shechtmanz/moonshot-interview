import pytest
from src.llm_api.chat_gpt import ChatGpt


# Warning: this test might break if shopbop.com changes their <metadata name="ROBOTS" Content="index, follow"> tag - consider mocking
def test_prompt():
    prompts = ["Is scraping www.etsy.com legal base on their terms and conditions. Summarize in one sentence", "Summarize it in one word, either yes or no"]
    chat = ChatGpt()
    for prompt in prompts:
        answer = chat.ask_chat(prompt)
        assert answer

