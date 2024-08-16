# 🔗 Simple Chain Program - Caching 🔗
# pip install langchain-community
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache  # allows caching the results
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Set up caching
set_llm_cache(InMemoryCache())

# Define the prompt template
template = """
    Write an essay on {topic} in 100 words.
    """ 
prompt_template = PromptTemplate(template=template)

# Initialize the language model
llm = ChatOpenAI(
    model='gpt-4o',
    max_tokens=100,
    temperature=0.7
)

# Create the LLM chain
llm_chain = prompt_template | llm

# Main loop for repeated execution
while True:
    topic = input("Enter your topic (or type 'exit', 'bye', or 'quit' to stop): ").strip()
    
    # Exit condition
    if topic.lower() in ['exit', 'bye', 'quit']:
        print("Goodbye!")
        break

    # Start time before invoking the chain
    start_time = time.time()

    # Invoke the chain with the given topic
    output = llm_chain.invoke({
        "topic": topic
    })

    # Print the output content
    print(output.content)

    # End time after the result is printed
    end_time = time.time()

    # Print the execution time
    print("\nExecution time: ", end_time - start_time)
