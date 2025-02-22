from langchain_google_genai import ChatGoogleGenetativeAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenetativeAI(model= "gemini-1.5-pro")

# this is the old method to talk to the LLM models
response = llm.invoke("What is the capital of india")

print(response)