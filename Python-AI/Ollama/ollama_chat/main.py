
import requests
import json

# Ollama Configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "phi3"

# Conversation History
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Provide clear and accurate answers."
        )
    }
]


def chat_completion(prompt: str) -> None:
    # Add the user's message to conversation history
    messages.append({
        "role": "user",
        "content": prompt
    })

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": True
    }

    assistant_response = ""

    try:
        with requests.post(
            OLLAMA_URL,
            json=payload,
            stream=True,
            timeout=(10, 300)
        ) as response:

            response.raise_for_status()

            print("\nAssistant: ", end="", flush=True)

            for line in response.iter_lines():
                if not line:
                    continue

                # Parse each JSON chunk from Ollama
                chunk = json.loads(line)

                if not isinstance(chunk, dict):
                    raise ValueError("Unexpected response format.")

                # Extract the generated content
                message = chunk.get("message", {})

                if not isinstance(message, dict):
                    raise ValueError("Invalid message format.")

                content = message.get("content", "")

                if content:
                    print(content, end="", flush=True)
                    assistant_response += content

                # Stop when Ollama finishes generating
                if chunk.get("done", False):
                    break

        print("\n")

        # Save only a completed assistant response
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

    except (requests.exceptions.RequestException,
            json.JSONDecodeError,
            ValueError) as error:

        # Remove the unanswered user message
        messages.pop()

        print(f"\nOllama error: {error}")

        # Note: Any partially streamed output is not saved
        # in conversation history.


def main():
    print("=" * 45)
    print("       OLLAMA LOCAL AI CHAT")
    print(f"       Model: {MODEL_NAME}")
    print("=" * 45)
    print("Type 'exit' to quit.")
    print("Type 'clear' to reset conversation history.")

    while True:
        try:
            prompt = input("\nYou: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

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
