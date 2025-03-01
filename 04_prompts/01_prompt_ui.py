from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate, load_prompt


st.header("Research Tool")


chat_model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")


paper_input = st.selectbox("Select Research Paper Name", ["Select..", "Attention is All you need", "Bert: Pre-training of Deep Bidirection Transformers","GPT-3: Language Model s are Few_Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", [ "Biginner Friendly", "Technical","Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select the explanation length", ["Short (1-2 paragraphs)", "Midium (3-5 paragraphs)", "Long (Detailed Explanation)"])

template = load_prompt("04_prompts/template.json")

# fill the template with variable
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})


if st.button("Summarize"):
    result = chat_model.invoke(prompt)
    st.markdown(result.content)
    # st.markdown("# Hello!")



