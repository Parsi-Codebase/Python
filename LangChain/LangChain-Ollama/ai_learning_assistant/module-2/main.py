from langchain_ollama import ChatOllama
from model_factory import create_model
class AILearningAssistant:
    def __init__(self,provider:str,model_name:str):
        self.model=create_model(
            provider=provider,
            model_name=model_name,
            temperature=0.3
        )
    def ask(self,question:str)->str:
        response=self.model.invoke(question)
        return response.content
    def stream(self,question:str):
        for chunk in self.model.stream(question):
            print(
                chunk.content,
                end='',
                flush=True
            )
def main():
        assistant=AILearningAssistant(provider='ollama',model_name='phi3')
        print("=" * 50)
        print("      AI LEARNING ASSISTANT")
        print("=" * 50)
        while True:
            question=input('\nYou: ')
            if question.lower() in ['exit','quit']:
                print('Goodbye!')
                break;
            try:
                answer=assistant.stream(question)
                print('\nAI')
                print(answer)
            except Exception as ex:
                print(f"\nError: {ex}")
if __name__=='__main__':
    main()
        
        