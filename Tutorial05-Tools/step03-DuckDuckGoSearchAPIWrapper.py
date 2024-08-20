from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
import re


#Applying filters
wrapper= DuckDuckGoSearchAPIWrapper(region='in-in', max_results=3, safesearch='moderate')
#source also referred to as 'backend'. The possible values are 'text' and 'news'
# text: This is the default value and retrieves standard text-based search results.
# news: This value fetches results specifically from news sources. 
search = DuckDuckGoSearchResults(api_wrapper=wrapper, source='news')
output = search.run('Latest news on Vinesh Phogat')

#Extracting Values - Snippet, Title and Link
def extract_info(output):
    pattern = r'\[snippet: (.*?), title: (.*?), link: (.*?)\]'
    matches = re.findall(pattern, output)
    
    extracted_info = []
    for match in matches:
        snippet, title, link = match
        extracted_info.append({
            'snippet': snippet,
            'title': title,
            'link': link
        })
    
    return extracted_info 

extracted_news = extract_info(output)
for news in extracted_news:
    print("*"*50)
    print("Snippet: ",news['snippet'])
    print("Title: ",news['title'])
    print("Link: ",news['link'])