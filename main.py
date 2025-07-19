import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# Initialize ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer the user's questions concisely."),
    ("user", "{question}")
])



# Create LangChain pipeline
chain = prompt | llm | StrOutputParser()

# Define request body model
class Question(BaseModel):
    question: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI LangChain Groq App! Use /ask to get answers."}

@app.post("/ask")
async def ask_question(q: Question):
    """
    Endpoint to ask a question to the LLM.
    """
    try:
        response = chain.invoke({"question": q.question})
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
