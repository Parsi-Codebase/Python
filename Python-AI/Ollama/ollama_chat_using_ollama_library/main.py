import ollama
MODEL_NAME='phi3'
messages=[
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Provide clear and accurate answers."
        )
    }
]
def chat_completion(prompt: str) -> None:
    """Send a prompt to Ollama and stream the response."""
    messages.append({
        "role": "user",
        "content": prompt
    })
    assistant_response = ""
    try:
        print("\nAssistant: ", end="", flush=True)
        # Call the Ollama Python library
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )

        # Read the response chunk by chunk
        for chunk in stream:
            content = chunk.message.content or ""

            if content:
                print(content, end="", flush=True)
                assistant_response += content

        print("\n")
        # Save the complete response to conversation history
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })
    except ollama.ResponseError as error:
        messages.pop()
        print(f"\nOllama model error: {error}")
    except Exception as error:
        messages.pop()
        print(f"\nError communicating with Ollama: {error}")
def main():
    print("=" * 45)
    print("       OLLAMA PYTHON CHAT")
    print(f"       Model: {MODEL_NAME}")
    print("=" * 45)
    print("Type 'exit' to quit.")
    print("Type 'clear' to reset conversation history.")

    while True:
        prompt = input("\nYou: ").strip()

        if not prompt:
            continue

        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        if prompt.lower() == "clear":
            messages[:] = messages[:1]
            print("Conversation history cleared.")
            continue

        chat_completion(prompt)


if __name__ == "__main__":
    main()
