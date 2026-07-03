# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import random
import argparse
import sys

def deepseek_input(message):
    # message = sys.stdin.read().strip()
    client = OpenAI(api_key="sk-c5b69a2435a54546815200ab6652903a", base_url="https://api.deepseek.com")
    # https://api-docs.deepseek.com/quick_start/parameter_settings
    random_seed = random.randint(1, 1000000)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": message},
        ],
        stream=False, 
        max_tokens=8192, 
        temperature=1.3, 
        seed=random_seed
    )
    return response.choices[0].message.content 


def deepseek_input_prompt(prompt, message):
    message = prompt + "\n" + message
    return deepseek_input(message)


if __name__ == "__main__":
    message = deepseek_input("Hello what weather do we have tody")
    print(message)