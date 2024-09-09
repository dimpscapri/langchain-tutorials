# pip install langchain-pinecone
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Pinecone
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

# See full prompt at https://smith.langchain.com/hub/rlm/rag-prompt
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    x = "\n\n".join(doc.page_content for doc in docs)
    print(x)
    return x

index_name = "chruchill-speech"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)
llm = ChatOpenAI(model="gpt-4o", max_tokens=200, temperature=0.7)

vector_store = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
# vector_store = PineconeVectorStore(index=index_name, embedding=embeddings)

query = 'Where should we fight?'

qa_chain = (
    {
        "context": vector_store.as_retriever() | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)
answer = qa_chain.invoke(query)
print(answer)
