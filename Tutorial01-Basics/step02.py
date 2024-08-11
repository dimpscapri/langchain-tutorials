#pip install langchain-openai
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()
#print(os.environ["OPENAI_API_KEY"])

llm = ChatOpenAI(model="gpt-4o")

#asking question
while True:
    question =input("Enter your query/type bye to exit: ")
    if question.lower() == 'bye':
        print("Thanks!")
        break
    else:
        answer = llm.invoke(question) #allows you to ask question from llm
        # print(answer)
        print(answer.content+"\n")

#Example: Who is the prime minister of Uk? 
#Notes: the model is trained only upto Oct 2023
#ChatGPT4o is a program based on openai which is connected to internet