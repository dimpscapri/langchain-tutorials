from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0,
    max_tokens=200
)

template = "Calculate the square root of the factorial of 12 and display it with 4 decimal points."
# prompt_template = PromptTemplate(template=template)
agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True
)
response = agent_executor.invoke(template)
print(response['output'])




