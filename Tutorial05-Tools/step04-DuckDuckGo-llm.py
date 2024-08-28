from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()
# Applying filters
wrapper = DuckDuckGoSearchAPIWrapper(
    region="in-in", max_results=3, safesearch="moderate"
)
# source also referred to as 'backend'. The possible values are 'text' and 'news'
# text: This is the default value and retrieves standard text-based search results.
# news: This value fetches results specifically from news sources.
search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")
output = search.run("Latest news on Kartik Aaryan.")


# Extracting Values - Snippet, Title and Link
def extract_info(output):
    pattern = r"\[snippet: (.*?), title: (.*?), link: (.*?)\]"
    matches = re.findall(pattern, output)

    extracted_info = []
    for match in matches:
        snippet, title, link = match
        extracted_info.append({"snippet": snippet, "title": title, "link": link})

    return extracted_info


extracted_news = extract_info(output)

template = """
You are a renowned news blogger known for crafting engaging and informative news articles in Hindi. Given the following details in English, your task is to create a compelling and well-structured news article in Hindi. Please write both the title and the news content in Hindi, ensuring that it captures the essence of the provided information while making it engaging for Hindi-speaking readers. Title should be very creative.

Details: {details}
"""

prompt_template = PromptTemplate(template=template)
# Initialize the language model
llm = ChatOpenAI(model="gpt-4o", max_tokens=500, temperature=0.7)

# Create the LLM chain
llm_chain = prompt_template | llm

result = llm_chain.invoke({"details": extracted_news})
# print(result.content)
with open("hindi-output.md", "w", encoding="utf-8") as file:
    # Write data to the file
    file.write(result.content)
