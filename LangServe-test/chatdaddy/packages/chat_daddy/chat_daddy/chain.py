from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "reply with a single emoji.",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{text}"),
    ]
)
# _model = ChatOpenAI()

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
# chain = _prompt | _model

chain = _prompt


