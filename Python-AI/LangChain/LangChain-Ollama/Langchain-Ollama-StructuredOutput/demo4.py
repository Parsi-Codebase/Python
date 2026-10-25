# multiple structured records
from pydantic import BaseModel
from langchain_ollama import ChatOllama

class InterviewQuestion(BaseModel):

    question: str
    difficulty: str
    answer: str


class InterviewQuestions(BaseModel):

    questions: list[InterviewQuestion]
model = ChatOllama(
    model="phi3",
    temperature=0.3
)
structured_model = model.with_structured_output(
    InterviewQuestions
)
result = structured_model.invoke(
    """
    Generate 5 interview questions about FastAPI.
    Include beginner, intermediate and advanced questions.
    """
)
for question in result.questions:

    print("Question:", question.question)
    print("Difficulty:", question.difficulty)
    print("Answer:", question.answer)
    print("-" * 50)