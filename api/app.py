from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn 
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API server"
)


model=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} in about 150 words.")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)