from dotenv import load_dotenv
from pinecone import Pinecone
from numpy import random

load_dotenv()

pc = Pinecone()
index_name = "langchain"

index = pc.Index(index_name)

num_vectors, num_dimension = 3, 1536
vectors = random.rand(num_vectors, num_dimension)

ids = list("xyz")

# Upsert vectors (insert/update)
index.upsert(zip(ids, vectors), namespace="np1")
# print(index.describe_index_stats())

# fetch 'x' from default namespace - it should not work
results = index.fetch(ids=['x'])
print(results)

# fetch 'x' from np1 namespace
results = index.fetch(ids=['x'], namespace='np1')
print(results)

# delete a vector from a namespace
# index.delete(ids=['x'])
# print(index.describe_index_stats())

index.delete(ids=['x'], namespace='np1')
print(index.describe_index_stats())

index.delete(delete_all=True, namespace='np1') #This will also delete the namespace
print(index.describe_index_stats())

