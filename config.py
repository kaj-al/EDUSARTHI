import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="meta-llama-3-8b-instruct",api_key=os.getenv("OPENAI_API_KEY"),base_url=os.getenv("OPENAI_API_URL"),temperature=0.5)