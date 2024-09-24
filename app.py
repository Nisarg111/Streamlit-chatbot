import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate([
    ("system","You are need to give answers"),
    ("user","{input}")
])

parser = StrOutputParser()

llm = ChatGroq(model="Llama-3.1-8b-Instant")
chain = prompt|llm|parser

st.title("Hello There Nisarg")
input = st.text_input("How may I Help You")

if input:
    res = chain.invoke(input)
    st.write(res)