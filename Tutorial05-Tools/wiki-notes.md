
# Difference between WikipediaAPIWrapper and WikipediaRetriever in LangChain

## WikipediaAPIWrapper

The **WikipediaAPIWrapper** is a utility in LangChain that directly interacts with the Wikipedia API. It is used to fetch concise information in the form of page summaries based on a specific query.

### Key Features:
- **Summarization**: Returns summaries of Wikipedia pages that match the query.
- **Parameters**: 
  - `doc_content_chars_max`: Limits the number of characters per document.
  - `top_k_results`: Specifies the number of top results to return.
  - `load_all_available_meta`: Determines whether to load additional metadata.
- **Use Case**: Best suited for retrieving quick summaries of Wikipedia articles without needing the full content.

### Example Usage:
```python
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

wrapper = WikipediaAPIWrapper()
summary = wrapper.run("Python programming language")
print(summary)
```

[Source](https://api.python.langchain.com/en/latest/utilities/langchain_community.utilities.wikipedia.WikipediaAPIWrapper.html)

## WikipediaRetriever

The **WikipediaRetriever** is a more extensive retriever designed to fetch multiple detailed documents from Wikipedia. It is part of LangChain's document retrieval system and is ideal for applications requiring more in-depth content.

### Key Features:
- **Comprehensive Retrieval**: Retrieves multiple documents that match the query.
- **Parameters**:
  - `load_max_docs`: Limits the number of documents to retrieve.
  - `lang`: Specifies the language of the Wikipedia edition to search.
  - `load_all_available_meta`: Includes additional metadata if set to `True`.
- **Use Case**: Ideal for scenarios where detailed information from multiple Wikipedia pages is required.

### Example Usage:
```python
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever()
documents = retriever.load("Artificial Intelligence")
for doc in documents:
    print(doc.page_content)
```

[Source](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.wikipedia.WikipediaLoader.html)

## Summary

- **WikipediaAPIWrapper** is designed for quick access to Wikipedia page summaries, making it suitable for brief overviews.
- **WikipediaRetriever** offers a deeper retrieval of multiple documents, which is more suitable for detailed analysis and comprehensive information gathering.

```

This file provides a concise comparison between `WikipediaAPIWrapper` and `WikipediaRetriever` in LangChain, along with example code snippets to illustrate their usage.