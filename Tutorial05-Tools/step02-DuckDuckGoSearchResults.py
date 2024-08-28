from langchain_community.tools import DuckDuckGoSearchResults


search = DuckDuckGoSearchResults()
output = search.run("Latest news on Vinesh Phogat")
print(output)  # step A - get results with metadata information
