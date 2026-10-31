import ollama

# System prompt
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Use previous conversation messages to answer questions. "
            "Remember information shared by the user during this conversation. "
            "If you do not know something, be honest."
        )
    }
]

print("Welcome to My AI Chatbot!")
print("Type /bye to exit.")

while True:

    user_input = input("You: ").strip()

    if user_input.lower() == "/bye":
        print("Bot: Goodbye!")
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages
    )

    assistant_message = response["message"]["content"]

    print("Bot:", assistant_message)

    messages.append({
        "role": "assistant",
        "content": assistant_message
    })