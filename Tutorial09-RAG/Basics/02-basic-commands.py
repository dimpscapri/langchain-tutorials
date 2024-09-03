from dotenv import load_dotenv
from pinecone import Pinecone
from numpy import random

load_dotenv()

pc = Pinecone()
index_name = "langchain"

index = pc.Index(index_name)

num_vectors, num_dimension = 5, 1536
vectors = random.rand(num_vectors, num_dimension)

# Following will typecast string to a list ['a', 'b', 'c', 'd', 'e']
ids = list("abcde")

# Upsert vectors (insert/update)
index.upsert(zip(ids, vectors))
print(index.describe_index_stats())
# print(vectors)

# Update a single vector 'c'
index.upsert(
    vectors=[("c", [random.rand()] * num_dimension)]
)  # Muliplying a list by number replicates its items in list

# fetching vectors
# print(index.fetch(ids=["c", "d"]))

# deleting vectors
# index.delete(ids=['c','d'])
# print(index.describe_index_stats())

# query
query_vector = random.rand(1, num_dimension).tolist()
# print(query_vector)

# query_vector = [rn.random() for i in range(1536)]
# print(query_vector)

result = index.query(vector=query_vector, top_k=3, include_values=False)
print(result)
