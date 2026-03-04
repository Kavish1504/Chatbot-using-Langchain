from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI assistant. Please respond to the user queries."),
    ("user", "Question:{question}")
])

st.title("Chatbot using Langchain")
input_text=st.text_input("Search the topic you want!!")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
