\# Local AI Chatbot using Ollama



\## Project Overview



This project is a locally running AI chatbot built using Python, Ollama, Llama 3.2 (1B), and Streamlit.



It allows users to interact with a Large Language Model (LLM) through a browser-based chat interface without requiring a paid cloud LLM API.



\## Technologies Used



\- Python

\- Ollama

\- Llama 3.2 (1B)

\- Streamlit

\- Ollama Python Client



\## Features



\- Interactive AI conversations

\- Locally running language model

\- Conversation history during a session

\- System prompt for assistant behaviour

\- Clear Chat functionality

\- Error handling for Ollama connection and model errors

\- Browser-based interface



\## Architecture



User → Streamlit UI → Python → Ollama → Llama 3.2 → Response



\## Project Structure



```text

ollama-chatbot/

│

├── venv/

├── app.py

├── chatbot.py

├── requirements.txt

└── README.md

```



\## Installation



\### 1. Install Ollama



Download Ollama from:



https://ollama.com/download



\### 2. Download the model



```bash

ollama pull llama3.2:1b

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the environment (Windows)



```cmd

venv\\Scripts\\activate

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\### 6. Run the chatbot



```bash

streamlit run app.py

```



Open the local URL displayed in your terminal, normally:



http://localhost:8501



\## Learning Outcomes



\- Understanding local LLM execution

\- Integrating Ollama with Python

\- Working with chat messages and system prompts

\- Managing conversation history with Streamlit session state

\- Building an interactive AI application

\- Handling application errors



\## Future Enhancements



\- Persistent conversation storage

\- Multiple model selection

\- Streaming AI responses

\- RAG-based document question answering

\- User authentication



\## Author



Developed as a hands-on project to learn Local LLM application development.



