import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path=".env.dev")

model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    SystemMessage(content="Translate the following from Vietnamese to English"),
    HumanMessage(content="Xin chào, tôi tên là Huy. Tôi đến từ Việt Nam."),
]

parser = StrOutputParser()

chain = model | parser

output = chain.invoke(messages)

print(output)
