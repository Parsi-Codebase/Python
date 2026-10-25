from langchain_ollama import ChatOllama
from model_factory import create_model
from prompts import learning_prompt
class AILearningAssistant:
    def __init__(self,provider:str,model_name:str):
        self.model=create_model(
            provider=provider,
            model_name=model_name,
            temperature=0.3
        )
    def explain(
        self,
        topic:str,
        language:str,
        level:str
    ):
        messages=learning_prompt.invoke({
            'topic':topic,
            'language':language,
            'level':level
        })
        print(messages)
        response=self.model.invoke(messages)
        return response.content
    
def main():
        assistant=AILearningAssistant(provider='ollama',model_name='phi3')
        print("=" * 60)
        print("      AI LEARNING ASSISTANT")
        print("=" * 60)
        while True:
            topic = input("\nTopic: ")
            language = input("Programming Language: ")
            level = input("Experience Level: ")
            if topic.lower() in ['exit','quit']:
                print('Goodbye!')
                break;
            try:
                answer=assistant.explain(topic,language,level)
                print('\nAI')
                print(answer)
            except Exception as ex:
                print(f"\nError: {ex}")
if __name__=='__main__':
    main()
        
        