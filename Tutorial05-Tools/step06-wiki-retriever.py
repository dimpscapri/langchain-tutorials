#pip install wikipedia
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever()
topic = input("Enter the topic you want to fetch: ")
docs = retriever.invoke(topic)
# print(len(docs))
# print(docs[-1].page_content[:400])

for doc in docs:
    print(doc.page_content)
#connect above to llm to fetch top 2 interesting facts about the output using llama and Google gemini
