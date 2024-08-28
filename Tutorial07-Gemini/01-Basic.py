# pip install langchain-google-genai
# pip install google-generativeai
from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

st.title("Ask Anything")

load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# for model in genai.list_models():
#     print(model.name)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.7)

# #asking question

question = st.text_input("Enter your query: ")

if st.button("Submit"):
    answer = llm.invoke(question)  # allows you to ask question from llm
    # print(answer)
    st.write("Your Answer:")
    st.write(answer.content + "\n")
