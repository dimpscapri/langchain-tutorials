#pip install langchain python-dotenv
from dotenv import load_dotenv
import os

#Loading key from enviornment
load_dotenv()
print(os.environ["OPENAI_API_KEY"])