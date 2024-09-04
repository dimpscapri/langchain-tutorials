from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from colorama import Fore, Back, Style, init
import tiktoken
from langchain_openai import OpenAIEmbeddings


load_dotenv()
init()  # initialzing colorama

with open("Tutorial09-RAG/Intermediate/files/churchill_speech.txt") as f:
    churchill_speech = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20, length_function=len
)

chunks = text_splitter.create_documents([churchill_speech])
print(f"{Fore.CYAN}Now you have {Fore.RED}{len(chunks)}{Fore.CYAN} chunks!")


def print_embedding_cost(chunks):
    enc = tiktoken.encoding_for_model("text-embedding-3-small")
    total_tokens = 0
    for chunk in chunks:
        total_tokens += len(enc.encode(chunk.page_content))
    print(f"{Fore.GREEN}Total Tokens: {Fore.RED}{total_tokens}")
    print(f"{Fore.GREEN}Embedding Cost:{Fore.RED} {total_tokens/1000 * 0.0004:.6f}")


# print_embedding_cost(chunks)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)
# vector = embeddings.embed_query('abc')
# vector = embeddings.embed_query(chunks[0].page_content)
# print(vector)
