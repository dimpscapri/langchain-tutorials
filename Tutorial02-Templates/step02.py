##Program - convert your prompt into funny prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
import os

load_dotenv()
# print(os.environ["OPENAI_API_KEY"])

llm = ChatOpenAI(
    model="gpt-4o", temperature=0.7
)  # temprature means the creativity level [0-1] #0 means less creative and 1 means more creative default is 0.7

parser = StrOutputParser()  # object of StrOutputParser
# asking question

# Create Prompt Template
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a famous comedian and you reply to every question in a funny way."
        ),
        HumanMessagePromptTemplate.from_template("My question is {question}"),
    ]
)

while True:
    question = input("Enter the type of your question/type bye to exit: ")
    if question.lower() == "bye":
        print("Thanks!")
        break
    else:
        messages = chat_template.format_messages(question=question)
        print(messages)
        answer = llm.invoke(messages)  # allows you to ask question from llm
        # print(parser.invoke(answer))
        # print(answer)
        print(answer.content)
