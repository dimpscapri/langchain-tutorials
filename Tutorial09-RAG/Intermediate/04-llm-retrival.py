# pip install langchain-pinecone
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Pinecone


load_dotenv()

index_name = "chruchill-speech"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)
llm = ChatOpenAI(model="gpt-4o", max_tokens=200, temperature=0.7)

vector_store = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
# vector_store = PineconeVectorStore(index=index_name, embedding=embeddings)
# print(vector_store)

retriever = vector_store.as_retriever(search_type = 'similarity', search_kwargs={'k':3})

chain = RetrievalQA.from_chain_type(llm = llm, chain_type='stuff', retriever=retriever)

query = 'Where should we fight?'
answer = chain.invoke(query)
print(answer['result'])
