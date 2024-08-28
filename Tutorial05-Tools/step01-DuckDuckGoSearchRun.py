# DuckDuckGo - DuckDuckGoSearchRun - it returns String only.
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
search = DuckDuckGoSearchRun()
search_result = search.invoke("Vinesh Phogat India Arrival Live Updates")
template = "create a summary based on following {topic}"
prompt_template = PromptTemplate(template=template)
# Initialize the language model
llm = ChatOpenAI(model="gpt-4o", max_tokens=300, temperature=0.7)

# Create the LLM chain
llm_chain = prompt_template | llm

result = llm_chain.invoke({"topic": search_result})
print(result.content)
