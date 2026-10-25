from langchain_ollama import ChatOllama
from model_factory import create_model
from prompts import learning_prompt
from langchain_core.messages import(
    SystemMessage,HumanMessage,AIMessage
)
from ai_learning_assistant import AILearningAssistant    
def main():
        assistant=AILearningAssistant(provider='ollama',model_name='phi3')
        print("=" * 60)
        print("      AI LEARNING ASSISTANT")
        print("=" * 60)
        topic = input("\nTopic: ")
        language = input("Programming Language: ")
        level = input("Experience Level: ")

        result = assistant.explain(
        topic=topic,
        language=language,
        level=level
    )

        print("\nTOPIC")
        print("-" * 60)
        print(result.topic)

        print("\nDIFFICULTY")
        print("-" * 60)
        print(result.difficulty)

        print("\nSUMMARY")
        print("-" * 60)
        print(result.summary)

        print("\nKEY POINTS")
        print("-" * 60)

        for point in result.key_points:
            print("-", point)

        print("\nEXAMPLE")
        print("-" * 60)
        print(result.example)

        print("\nREAL-WORLD USAGE")
        print("-" * 60)
        print(result.real_world_usage)
    
if __name__ == "__main__":
    main()

      
        

        
        