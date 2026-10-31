
import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="My Local AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# System prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer questions clearly and accurately.
Use previous conversation messages as context.
"""

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

# Header
col1, col2 = st.columns([4, 1])

with col1:
    st.title("🤖 My Local AI Chatbot")
    st.caption("Powered by Ollama and Llama 3.2 (1B)")

with col2:
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
        st.rerun()

# Display conversation history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=st.session_state.messages
                )

                bot_response = response["message"]["content"]

                st.markdown(bot_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_response
                })

            except ollama.ResponseError as e:

                if e.status_code == 404:
                    st.error(
                        "Model not found. Please check your Ollama model."
                    )
                else:
                    st.error(f"Ollama error: {e.error}")

            except Exception as e:
                st.error(
                    "Unable to connect to Ollama. "
                    "Please check whether Ollama is running."
                )

                st.caption(f"Technical details: {e}")
