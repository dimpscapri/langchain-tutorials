#pip install langchain-ollama
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=5000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

topic = input("Enter the topic you want to fetch: ")
output = wiki.invoke({'query':topic})
#wiki.invoke(topic) -- this is another way to invoke
# print(output)
#
#Integration with Llama 3.1
template = """
Retrieve two fascinating and unique facts about {output} that will captivate the 
reader's interest.
"""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1", verbose=True)

chain = prompt | model

response = chain.invoke({"output": output})
print(response)

#connect above to llm to fetch top 2 interesting facts about the output using llama and Google gemini
