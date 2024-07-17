import os
import logging

from typing import Any, Dict, Annotated, Literal
from typing_extensions import TypedDict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableConfig, RunnableLambda
# from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.embeddings import Embeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.graph import StateGraph
from langgraph.graph.graph import END, START
from langgraph.graph.message import add_messages

# from langserve import add_routes
# Add LangServe routes to the app
# add_routes(fastapi_app, NotImplemented)



# os.environ['USER_AGENT'] = 'langchain'
fastapi_app = FastAPI()




class GraphState(TypedDict):
    input: str
    messages: Annotated[list, add_messages]
    generation: str
    web_search: str
    documents: list[str]




def call_ollama(state: GraphState, config: RunnableConfig):
    logging.debug("NODE: friendly_chatbot()")

    # llm = ChatOllama(model=config['hyperparameters']['llm_model'], temperature=0.8)
    llm = ChatOllama(model="phi3:latest", temperature=0.8)

    # messages = '\n'.join(f"{message.type}: {message.content}" for message in state["messages"])
    input = state["input"]

    prompt = PromptTemplate(
        template="""You are an expert at changing the topic back to cats.  Always take the user's query and relate it back to cats.

---

{input}
""",
        input_variables=["messages"])


    chain = prompt | llm

    this_config = config
    this_config['metadata']['node_type'] = "output"

    bot_reply = chain.invoke({"input": input}, config=this_config)
    print("=======================")
    print(bot_reply)
    return {"messages": [AIMessage(content=bot_reply.content)]}






def compiled_graph():

    # Define the LangGraph workflow
    graph = StateGraph(GraphState)
    graph.add_node("call_ollama", call_ollama)
    graph.set_entry_point("call_ollama")
    # graph.add_edge(START, call_ollama)
    graph.add_edge("call_ollama", END)

    compiled_graph = graph.compile()
    return compiled_graph




# Define Pydantic model for request body
class UserQuery(BaseModel):
    input: str


# Add a route to test the generate node directly
@fastapi_app.post("/generate")
async def generate_route(request: UserQuery):
    state = {
        "input": request.input,
        "documents": [],
        "generation": "",
        "web_search": "",
    }
    # try:
        # compiled_graph().stream(state)
        # return {"result": outputs}
    
    graph = compiled_graph()
    res = graph.stream(state)
    return {"result": res}
    # except Exception as e:
        # print(e)
        # raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # os.environ['LANGCHAIN_LOG_LEVEL'] = 'DEBUG'
    # logging.basicConfig(level=os.environ.get("LANGCHAIN_LOG_LEVEL", "INFO"))

    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=5001)
