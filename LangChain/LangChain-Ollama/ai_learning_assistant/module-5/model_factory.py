from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
def create_model(
  provider:str,
  model_name:str,
  temperature:float=0.3  
):
    if provider.lower()=='ollama':
        return ChatOllama(
            model=model_name,
            temperature=temperature
        )
    elif provider=='openai':
        return ChatOpenAI(
            model=model_name,
            temperature=temperature
        )
    else:
        raise ValueError(
        f'Unsupported provider:{provider}'
    )