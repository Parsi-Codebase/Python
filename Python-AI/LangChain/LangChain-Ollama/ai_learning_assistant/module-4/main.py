from langchain_ollama import ChatOllama
from model_factory import create_model
from prompts import learning_prompt
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
    
def main():
        assistant=AILearningAssistant(provider='ollama',model_name='phi3')
        print("=" * 60)
        print("      AI LEARNING ASSISTANT")
        print("=" * 60)
        while True:
            question = input("\nYou: ")
            
            if question.lower() in ['exit','quit']:
                print('Goodbye!')
                break;
            try:
                answer=assistant.chat(question)
                print('\nAI')
                print(answer)
            except Exception as ex:
                print(f"\nError: {ex}")
if __name__=='__main__':
    main()
        
        