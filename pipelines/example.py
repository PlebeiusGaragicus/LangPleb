from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
from schemas import OpenAIChatMessage
import requests

import asyncio
from typing import Callable, Awaitable, Any


# from subprocess import call

# Model ID: echo_bot
# Message: asdf
body = {
    'stream': True,
    'model': 'echo_bot',
    'messages': [
        {
            'role': 'user',
            'content': 'asdf'
            },
        {
            'role': 'assistant',
            'content': '\n```sh\necho "Hello, I am an echo bot. You said: {user_message}"\n```'
            }
    ],
    'chat_id': '4f3c5a49-a91b-4736-9f06-8d39e9ad15ee',
    'user': {
        'name': 'admin',
        'id': 'b1e31733-d29f-407a-a43a-0de19cfc84a6',
        'email': 'admin@admin.com',
        'role': 'admin'
    }
}



class Pipeline:
    class Valves(BaseModel):
        number: str

    def __init__(self):
        # the name of the pipeline (AKA construct) in the UI
        self.name = "echobot"

        # Initialize
        self.valves = self.Valves(
            **{
                "number": "1"
                # "pipelines": ["*"],                                 # Connect to all pipelines
                # "DB_HOST": os.environ["PG_HOST"],                   # Database hostname
                # "DB_PORT": os.environ["PG_PORT"],                   # Database port 
                # "DB_USER": os.environ["PG_USER"],                   # User to connect to the database with
                # "DB_PASSWORD": os.environ["PG_PASSWORD"],           # Password to connect to the database with
                # "DB_DATABASE": os.environ["PG_DB"],                 # Database to select on the DB instance
                # "DB_TABLES": ["albums"],                            # Table(s) to run queries against 
                # "OLLAMA_HOST": "http://host.docker.internal:11434", # Make sure to update with the URL of your Ollama host, such as http://localhost:11434 or remote server address
                # "TEXT_TO_SQL_MODEL": "phi3:latest"                  # Model to use for text-to-SQL generation      
            }
        )

    async def on_startup(self):
        print(f"loading pipeline: {self.name}")

    async def on_shutdown(self):
        print(f"unloading pipeline: {self.name}")


    async def pipe(self, __event_emitter__: Callable[[dict], Awaitable[None]],
             user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print("laying our pipe out here!")



        if body.get("title", False):
            print("Title Generation")
            return "We fuck pipes, yo!"


        else:
            if "user" in body:
                print("######################################")
                print(f'# Body: {body}')
                print(f"# Model ID: {model_id}")
                print(f"# Message: {user_message}")
                print(f'# Messages: {messages}')

                print("######################################")

                await __event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "status": "in_progress",
                        "description": "Retrieving user data",
                        "done": False,
                    },
                })

                await asyncio.sleep(4)

                await __event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "status": "complete",
                        "description": "User data retrieved successfully",
                        "done": True,
                    },
                })



            # commands = user_message.split(" ")

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
                # return "..."
                return """
```sh
echo "Hello, I am an echo bot. You said: {user_message}"
```
"""
            except Exception as e:
                return f"Error: {e}"
