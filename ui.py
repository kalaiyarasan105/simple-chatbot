import streamlit as st
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8000/ask"


st.title("🤖 AI ChatBot")

# User input
user_question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if user_question:
        try:
            # Send POST request to FastAPI
            response = requests.post(FASTAPI_URL, json={"question": user_question})
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            answer = response.json().get("answer")
            st.write("### Answer:")
            st.write(answer)
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the FastAPI backend. Please ensure it is running at http://localhost:8000.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")