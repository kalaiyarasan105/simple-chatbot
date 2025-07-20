import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from pydantic import BaseModel
import threading

# Load .env
load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# Initialize Groq Chatbot
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

# Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}")
])

# Create processing chain
chain = prompt | llm | StrOutputParser()

# ------------------- FastAPI Server (optional) -------------------

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "FastAPI is working! Use POST /ask or the terminal."}

@app.post("/ask")
async def ask(q: Question):
    try:
        response = chain.invoke({"question": q.question})
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}

# ------------------- Terminal Chatbot Loop -------------------

def terminal_chat():
    print("\n🤖 Terminal Chatbot Ready (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("👋 Exiting chatbot.")
            break
        try:
            response = chain.invoke({"question": user_input})
            print(f"Bot: {response}\n")
        except Exception as e:
            print("❌ Error:", str(e))

# ------------------- Main Run -------------------

if __name__ == "__main__":
    # Start FastAPI in a separate thread
    def run_server():
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)

    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Run terminal chat loop
    terminal_chat()
