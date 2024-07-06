from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
import requests


from subprocess import call


class Pipeline:
    def __init__(self):
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "applescript_pipeline"
        self.name = "Template Pipeline"


    async def on_startup(self):
        # This function is called when the server is started.
        print("yo bitch we startin' shit!")


    async def on_shutdown(self):
        # This function is called when the server is stopped.
        print("yo bitch, I'm out!")


    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print("laying our pipe out here!")



        if body.get("title", False):
            print("Title Generation")
            return "We fuck pipes, yo!"


        else:
            if "user" in body:
                print(body)
                print("######################################")
                print(f'# Body: {body}')
                print(f"# Model ID: {model_id}")
                print(f"# Message: {user_message}")
                print(f'# Messages: {messages}')

                print("######################################")

            commands = user_message.split(" ")

            # payload = {
            #     "model": MODEL,
            #     "messages": [
            #         {
            #             "role": "system",
            #             "content": f"You are an agent of the AppleScript Pipeline. You have the power to control the volume of the system.",
            #         },
            #         {"role": "user", "content": user_message},
            #     ],
            #     "stream": body["stream"],
            # }

            # try:
            #     r = requests.post(
            #         url=f"{OLLAMA_BASE_URL}/v1/chat/completions",
            #         json=payload,
            #         stream=True,
            #     )

            #     r.raise_for_status()

            #     if body["stream"]:
            #         return r.iter_lines()
            #     else:
            #         return r.json()

            try:
                return "yo you what up"
            except Exception as e:
                return f"Error: {e}"
