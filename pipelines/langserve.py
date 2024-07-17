from typing import List, Union, Generator, Iterator
import requests


# from subprocess import call


class Pipeline:
    def __init__(self):
        self.name = "EchoPipe"


    async def on_startup(self):
        print(">>> THE ECHOPIPE PIPELINE IS STARTING!!! <<<")


    async def on_shutdown(self):
        print(">>> THE ECHOPIPE PIPELINE IS SHUTTING DOWN!!! <<<")


    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:
        print(">>> THE ECHOPIPE PIPELINE IS LAYING PIPE!!! <<<")

        if body.get("title", False):
            print(">>> THE ECHOPIPE PIPELINE IS GENERATING A TITLE!!! <<<")
            return "EchoPipe title"


        if "user" not in body:
            return

        print(body)
        print("######################################")
        print(f'# Body: {body}')
        print(f"# Model ID: {model_id}")
        print(f"# Message: {user_message}")
        print(f'# Messages: {messages}')

        print("######################################")

        # commands = user_message.split(" ")

        requests.post("http://localhost:5001/generate", json={"input": user_message})

        try:
            return f"EchoPipe: {user_message}"
        except Exception as e:
            return f"Error: {e}"
