# For demo of Similarity Search only
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings

# import pinecone

# pc = pinecone.Pinecone()
load_dotenv()

index_name = "chruchill-speech"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)

vector_store = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)

query = 'Where should we fight?'
result = vector_store.similarity_search(query)
print(result)