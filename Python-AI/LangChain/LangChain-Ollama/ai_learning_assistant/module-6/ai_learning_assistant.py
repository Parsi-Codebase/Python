from langchain_ollama import ChatOllama
from model_factory import create_model
from prompts import learning_prompt
from schemas import TopicExplanation
from langchain_core.messages import(
    SystemMessage,HumanMessage,AIMessage
)
class AILearningAssistant:
    def __init__(self,provider:str,model_name:str):
        self.model=create_model(
            provider=provider,
            model_name=model_name,
            temperature=0.3
        )
        self.structured_model=(
            self.model.with_structured_output(
                TopicExplanation
            )
        )
        self.chain=(learning_prompt | self.structured_model)
        self.history=[
            SystemMessage(
                content="""
                You are an experienced Python and AI instructor.

                Explain technical concepts clearly.
                Use practical examples.
                Provide code when appropriate.
                Keep explanations structured.
                """
            )
        ]
    def chat(self,question:str):
        self.history.append(
            HumanMessage(content=question)
        )
        response=self.model.invoke(self.history)
        self.history.append(
            AIMessage(content=response.content)
        )
        return response.content
    def explain(
        self,
        topic: str,
        language: str,
        level: str
    ):

       

        result = self.chain.invoke(
            {
            "topic": topic,
            "language": language,
            "level": level
        }
        )

        return result
    
