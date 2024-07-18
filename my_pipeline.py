import json
import requests
from subprocess import call
from pydantic import BaseModel
from typing import List, Union, Generator, Iterator, Optional
# from schemas import OpenAIChatMessage


VERSION = "0.0.1"

HELP_MESSAGE = """
This is the HELP MESSAGE :)

I jope you liek! 👨🏻‍💻
"""

USAGE = """
Commands: /version, /help, /usage, /info
"""

COMMAND_NOT_FOUND = """Command not found.  Try `/usage` for a list of commands."""





def assert_commands(user_message: str, model_id: str, messages: List[dict], body: dict):
    """ Asserts if the user message is a command.
    """
    if not user_message.startswith("/"):
        return (False, None)

    split = user_message.split(" ")
    command = split[0][1:].lower() # Remove the slash and take the first word

    if command == "version":
        return (True, f"Version {VERSION}")

    elif command == "help":
        return (True, HELP_MESSAGE)
    
    elif command == "usage":
        return (True, USAGE)
    
    elif command == "debug":
        return (True, f"# body:\n```json\n{json.dumps(body, indent=4)}\n```\n# model_id:\n```txt\n{model_id}\n```\n\n# messages:\n```json\n{json.dumps(messages, indent=4)}\n```")



    else:
        # return (False, None) # we can just have the llm/graph handle this... but the reply is usually non-sense as it lacks context and awareness that this was a "missed" command
        return (True, COMMAND_NOT_FOUND)






def everything(user_message: str, model_id: str, messages: List[dict], body: dict):

    is_command, command_response = assert_commands(user_message, model_id, messages, body)

    if is_command:
        return command_response

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": f"You are an agent of the AppleScript Pipeline. You have the power to control the volume of the system.",
            },
            {"role": "user", "content": user_message},
        ],
        "stream": body["stream"],
    }
    r = requests.post(
                    url=f"{OLLAMA_BASE_URL}/v1/chat/completions",
                    json=payload,
                    stream=True,
                )

    r.raise_for_status()

    if body["stream"]:
        return r.iter_lines()
    else:
        return r.json()





# OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_BASE_URL = "http://host.docker.internal:11434"
MODEL = "llama3:latest"



class Pipeline:
    class Valves(BaseModel):
            some_number: int = 0
            some_string: List[str] = ["user"]
            optional_number: Optional[int] = None




    def __init__(self):
        self.name = "AppleScript Pipeline"
        self.valves = self.Valves(
            **{
                "some_number": 10,
            }
        )

    async def on_startup(self):
        print(f">>> PIPELINE {self.name.upper()} IS STARTING!!! <<<")

    async def on_shutdown(self):
        print(f">>> PIPELINE {self.name.upper()} IS SHUTTING DOWN!!! <<<")




    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:

        print("######################################")
        print(f">>> PIPELINE '{self.name}' RUNNING")
        print(f"pipe filename: {__name__}")
        print("######################################")
        print(f"user_message: str\n{user_message}")
        print(f"model_id: str\n{model_id}")
        print(f"messages: List[dict]\n{messages}")
        print(f"body: dict\n{json.dumps(body, indent=4)}")
        print("######################################")

        if body.get("title", False):
            print("Title Generation")
            return "AppleScript Pipeline"

        try:
            return everything(user_message=user_message, body=body, model_id=model_id, messages=messages)

        except Exception as e:
            return f"Error: {e}"
