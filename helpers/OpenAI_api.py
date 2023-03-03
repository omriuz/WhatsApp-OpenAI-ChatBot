import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [
    {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely "
                                  "as possible. Knowledge cutoff: {3.3.2023} Current date: {3.3.2023}"}]


def text_completion(prompt: str) -> dict:
    try:
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        text = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": text})
        return {
            'status': 1,
            'response': text
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
