from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

vector = embedding.embed_query(text)

print(f"vecto of text: {str(vector)}")

doc = ["India is beautiful country", "capital of india is New Delhi", "Delhi is face high pollution problems"]

vector_2 = embedding.embed_documents(doc)

print(f"vector of docs: {str(vector_2)}")