from typing import List, Union, Generator, Iterator


HELP_TEXT = """
This is the EchoPipe pipeline. It is a simple pipeline that echoes back the user's message.


"""



class Pipeline:
    def __init__(self):
        self.name = "EchoBot"


    async def on_startup(self):
        print(f">>> PIPELINE {self.name.upper()} IS STARTING!!! <<<")


    async def on_shutdown(self):
        print(f">>> PIPELINE {self.name.upper()} IS SHUTTING DOWN!!! <<<")


    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:
        print("######################################")
        print(f">>> PIPELINE {self.name.upper()} IS LAYING PIPE!!! <<<")
        print(f'>>> Body: {body}')
        print(f">>> Model ID: {model_id}")
        print(f">>> user_message: {user_message}")
        print(f'>>> Messages: {messages}')

        if body.get("title", False):
            print("######################################")
            print(f">>> PIPELINE {self.name.upper()} IS GENERATING A TITLE!!! <<<")
            return "EchoBot"

        if "user" not in body:
            return


        # commands = user_message.split(" ")

        try:
            return f"EchoPipe: {user_message}"
        except Exception as e:
            return f"Error: {e}"
