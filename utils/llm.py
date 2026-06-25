import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# print("API Key Found:", bool(os.getenv("GROQ_API_KEY")))

def get_llm():

    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="openai/gpt-oss-120b",
        temperature=0.2
    )