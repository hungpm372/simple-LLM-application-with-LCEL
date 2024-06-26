import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path=".env.dev")

model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_template = "You are a helpful assistant that can translate between Vietnamese and English."
human_template = "{text}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", human_template)]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

while True:
    user_input = input("Human: ")
    if user_input.lower() == "exit":
        break
    output = chain.invoke({"text": user_input})
    print(f"Assistant: {output}")