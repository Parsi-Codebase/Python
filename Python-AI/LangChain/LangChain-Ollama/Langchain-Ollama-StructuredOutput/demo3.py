from pydantic import BaseModel
from langchain_ollama import ChatOllama

class QuizQuestion(BaseModel):

    question: str
    options: list[str]
    correct_answer: str
    explanation: str
    difficulty: str
    
model = ChatOllama(
    model="phi3",
    temperature=0.3
)

structured_model = model.with_structured_output(
    QuizQuestion
)
result = structured_model.invoke(
    """
    Create a multiple-choice question about Python decorators
    for a beginner.
    """
)

print(result)

print("Question:", result.question)

print("Options:")

for option in result.options:
    print("-", option)

print("Answer:", result.correct_answer)

print("Explanation:", result.explanation)