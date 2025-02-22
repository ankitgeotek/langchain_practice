from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

response = chat_model.invoke("What is capital of India?")

print(f"full_response: {response}\n")

print(f"content_of_response: {response.content}\n")
