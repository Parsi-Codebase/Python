from langchain_core.prompts import ChatPromptTemplate


learning_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an experienced programming instructor.

        Your responsibilities:
        - Explain concepts clearly.
        - Use simple language.
        - Provide practical examples.
        - Include code when appropriate.
        - Mention common mistakes.
        """
    ),
    (
        "human",
        """
        Explain the following topic:

        Topic: {topic}

        Programming Language: {language}

        Experience Level: {level}

        Structure the response as:

        1. Definition
        2. Explanation
        3. Example
        4. Real-world usage
        5. Common mistakes
        """
    )
])