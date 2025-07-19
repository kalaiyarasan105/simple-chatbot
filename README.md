Simple-Chat-Bot
A simple command-line chat bot application built with Python. This bot can engage in basic conversations, respond to user input, and provide information based on predefined rules.

Features
Interactive Command-Line Interface: Engage with the bot directly from your terminal.
Basic Conversational Abilities: Responds to greetings, questions, and common phrases.
Extensible: Easily add new rules and responses to expand the bot's knowledge.
Installation
To set up the Simple-Chat-Bot on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/MEERAN2314/Simple-Chat-Bot.git
cd Simple-Chat-Bot
Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

pip install -r requirements.txt
Usage
To run the chat bot, you have two options:

Command-Line Interface (CLI)
To interact with the bot via the command line, execute the main.py file:

python main.py
The bot will start, and you can begin interacting with it by typing messages into the terminal.

FastAPI (Web Interface)
If you want to run the bot as a web service using FastAPI, use the following command:

uvicorn main:app --reload
This will start the FastAPI server, typically accessible at http://127.0.0.1:8000.

Streamlit UI
To run the Streamlit-based user interface, use the following command:

streamlit run ui.py
This will open the Streamlit application in your web browser, usually at http://localhost:8501.

Technologies Used
Python
ui.py (for Streamlit user interface interactions)
main.py (main application logic, including FastAPI integration)
requirements.txt (for dependency management)
FastAPI
Streamlit
