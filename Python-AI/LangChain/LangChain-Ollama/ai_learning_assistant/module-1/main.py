from langchain_ollama import ChatOllama
class AILearningAssistant:
    def __init__(self,model_name:str):
        self.model=ChatOllama(
            model=model_name
        )
    def ask(self,question:str)->str:
        response=self.model.invoke(question)
        return response.content
def main():
        assistant=AILearningAssistant(model_name='phi3')
        print("=" * 50)
        print("      AI LEARNING ASSISTANT")
        print("=" * 50)
        while True:
            question=input('\nYou: ')
            if question.lower() in ['exit','quit']:
                print('Goodbye!')
                break;
            try:
                answer=assistant.ask(question)
                print('\nAI')
                print(answer)
            except Exception as ex:
                print(f"\nError: {ex}")
if __name__=='__main__':
    main()
        
        