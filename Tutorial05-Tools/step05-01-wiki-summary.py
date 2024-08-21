#pip install wikipedia
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=5000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

topic = input("Enter the topic you want to fetch: ")
output = wiki.invoke({'query':topic})

#wiki.invoke(topic) -- this is another way to invoke

print(output)
#connect above to llm to fetch top 2 interesting facts about the output using llama and Google gemini
