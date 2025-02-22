from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face API Token is missing!")
else:
    print("API_KEY_LOADED")

llm = HuggingFaceEndpoint(
    repo_id=  "TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # which model you want to use
    task = "text-generation" # what task you want to perform by the selected model
)

chat_model = ChatHuggingFace(llm = llm)

response = chat_model.invoke("What is the Capital of India?")

print(response.content)
