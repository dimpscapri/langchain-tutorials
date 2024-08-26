#pip install langchainhub
# pip install langsmith  (This is required for hub)
# To get langsmith key, go to https://smith.langchain.com/
from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import Tool, AgentExecutor, initialize_agent, create_react_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
# from langchain_openai import ChatOpenAI  

st.title("Ask Anything")

load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"]) 
# for model in genai.list_models():
#     print(model.name)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.7)
# llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

st.title("Enter your question")
# #asking question
question =st.text_input("Your question here...")

template ="""
    Answer the following question as best as you can
    Question: {question}
"""
prompt_template = PromptTemplate.from_template(template=template)
prompt = hub.pull('hwchase17/react')
# print(type(prompt))
# print(prompt.input_variables)
# print(prompt_template)
if st.button("Submit"):
    # 1. Python REPL TOOL (for executing Python Code)
    python_tool = PythonREPLTool()
    python_repl_tool = Tool(
        name = 'Python REPL',
        func = python_tool.run,
        description='Useful when you need to use Python to answer a question. You should input Python code.'
    )


    # 2. Wikipedia Tool (for searching Wikipedia)
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=5000)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    wiki_tool = Tool(
        name = 'Wikipedia',
        func = wiki.run,
        description='Useful when you need to look up a topic, country or person on Wikipedia'
    )



    # 3. DuckDuckGoSearch Tool (for general web searches) 
    duckduckgo_wrapper= DuckDuckGoSearchAPIWrapper(region='in-in', max_results=3, safesearch='moderate')
    duckduckgo_search = DuckDuckGoSearchResults(api_wrapper=duckduckgo_wrapper, source='news')
    duckduckgo_tool = Tool(
        name = 'DuckDuckGo',
        func = duckduckgo_search.run,
        description='Useful when you need to find information that another tool can\'t provide.'

    )

    tools = [python_repl_tool, wiki_tool, duckduckgo_tool]
    agent = create_react_agent(llm=llm, tools=tools,prompt=prompt)
    agent_executor = AgentExecutor(
        agent = agent,
        tools = tools,
        verbose = True,
        handle_parsing_errors = True,
        max_iterations = 10
    )

    output = agent_executor.invoke({
        'input': prompt_template.format(question=question)
    })
    st.write(output['output'])
