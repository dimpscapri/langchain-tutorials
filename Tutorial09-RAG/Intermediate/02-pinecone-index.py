from dotenv import load_dotenv
import pinecone
from langchain_community.vectorstores import Pinecone
from split_embed_text import chunks, embeddings  # calling existing code


pc = pinecone.Pinecone()

# Deleting all indexes
for i in pc.list_indexes().names():
    print("Deleting all indexes...", end="")
    pc.delete_index(i)
    print("Done")

# Creating new index
index_name = "chruchill-speech"
if index_name not in pc.list_indexes().names():
    print(f"Creating index {index_name}")
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=pinecone.ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print("Index created 😊")

vector_store = Pinecone.from_documents(chunks, embeddings, index_name=index_name)

vector_store = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
