# 🔗 Simple Chain Program - Personal Travel Guide - Streaming 🔗
################USER INPUTS#####################
# 🎨 Likes: art, history
# 🚫 Dislikes: crowds, loud noises
# 🏛️ Interests: museums, historical landmarks
# 🌿 Activity Types: relaxed, educational
# 📅 Travel Dates: April 10-15
# 🌍 City: Rome
################################################

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()
template = """
    You are a travel expert with extensive knowledge of cities around the world. A user has provided the following preferences:
    
    Likes: {likes}
    Dislikes: {dislikes}
    Interests: {interests}
    Preferred Activity Types: {activity_types}
    Travel Dates: {travel_dates}
    
    Based on these preferences, the user would like to visit {city}. Please suggest 5 unique and interesting places to visit in {city}, including details about why each place matches the user's preferences.
    """

prompt_template = PromptTemplate(template=template)

llm = ChatOpenAI(model="gpt-4o", max_tokens=200, temperature=0.7)

llm_chain = prompt_template | llm

output = llm_chain.stream(
    {
        "likes": input("Enter your likes: "),
        "dislikes": input("Enter your dislikes: "),
        "interests": input("Enter your interests: "),
        "activity_types": input("Enter your preferred activity type: "),
        "travel_dates": input("Enter travel dates: "),
        "city": input("Enter preferred city or place: "),
    }
)

for chunk in output:
    print(chunk.content, end="", flush=True)
    # flush=True: This forces the immediate display of the printed content,
    # ensuring that it appears on the screen as soon as it's printed,
    # without waiting for the buffer to fill up.
