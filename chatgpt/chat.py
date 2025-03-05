import time
from os import error
import yaml
from openai import OpenAI


def get_api_key():
    """
    获取 api key
    :return: string
    """
    config_file = '../env/env.yaml'
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        openapi = config.get('openai', {})
    return openapi.get('app_key', '')


api_key = get_api_key()
client = OpenAI(api_key=api_key)


def generate_text(question):
    """
    ChatGpt 文本模型
    :param question: prompt
    :return:
    """
    try:
        response = client.chat.completions.create(
            messages=[
                {'role': 'user', 'content': question},
            ],
            model='gpt-4o-mini',
            # stream=False
            stream=True,
            max_tokens=1024
        )

        # stream=False的时候，打开这个，启用非流式返回
        # print(response.choices[0].message.content)

        # stream=True的时候，启用流示返回
        for chunk in response:
            print(chunk.choices[0].delta.content, end="", flush=True)
    except error:
        time.sleep(10)
        return generate_text(prompt)


if __name__ == '__main__':
    while True:
        print(" ")
        prompt = input("BootAI：")
        generate_text(prompt)
        time.sleep(1)
