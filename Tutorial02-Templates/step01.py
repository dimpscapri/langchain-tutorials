#PROJECT - 01 SUGGEST BUSINESS NAMES
#Program - Given the type of the business it will suggest creative business names
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate  #import prompt template
import os

load_dotenv()
#print(os.environ["OPENAI_API_KEY"])

llm = ChatOpenAI(model="gpt-4o", temperature=0.7) #temprature means the creativity level [0-1] #0 means less creative and 1 means more creative default is 0.7
 
parser = StrOutputParser() #object of StrOutputParser
#asking question

#Create Prompt Template
template = """
    You are an expert in suggesting creative business names given the business type. 
    Suggest 5 creative names for the business type {business_type}
"""
prompt_template = PromptTemplate.from_template(template=template)
while True:
    business_type =input("Enter the type of your business/type bye to exit: ")
    if business_type.lower() == 'bye':
        print("Thanks!")
        break
    else:
        prompt = prompt_template.format(business_type=business_type)
        print(prompt)
        answer = llm.invoke(prompt) #allows you to ask question from llm
        # print(parser.invoke(answer))
        # print(answer)
        print(answer.content)

# content="Absolutely, I'd be happy to help! Here are five creative business names for a fruit-related business:\n\n1. **Fruitful Delights**\n2. **Juicy Harvest Haven**\n3. **Tropical Treasure Trove**\n4. **Vibrant Orchard**\n5. **Citrus & Berry Bliss**\n\nEach of these names aims to evoke freshness, variety, and the natural appeal of fruits." response_metadata={'token_usage': {'completion_tokens': 81, 'prompt_tokens': 36, 'total_tokens': 117}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_3aa7262c27', 'finish_reason': 'stop', 'logprobs': None} id='run-c92ae18f-386d-451e-9497-783a8ff7f0ea-0' usage_metadata={'input_tokens': 36, 'output_tokens': 81, 'total_tokens': 117}