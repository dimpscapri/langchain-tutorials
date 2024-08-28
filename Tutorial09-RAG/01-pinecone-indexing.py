# pip install pinecone-client
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

pc = Pinecone()
index_name = "langchain"
if index_name not in pc.list_indexes().names():
    print("Creating new index", index_name)
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print("Index created 😊")
else:
    print(f"Index {index_name} already exists!!!")
# print(pc.list_indexes())

index = pc.Index(index_name)
print(index.describe_index_stats())

# pc.delete_index(index_name)   allows you to delete the index
