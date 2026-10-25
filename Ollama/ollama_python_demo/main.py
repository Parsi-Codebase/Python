import requests
OLLAMA_URL='http://localhost:11434/api/chat'
MODEL_NAME='phi3'
def ask_llm(prompt:str)->str:
    payload={
        'model':MODEL_NAME,
        'messages':[
            {
                'role':'user',
                'content':prompt
            },   
        ],
           'stream':False
    }
    response=requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )
    response.raise_for_status()
    result=response.json()
    return result['message']['content']
if __name__=='__main__':
    prompt=input('Enter u r prompt: ')
    answer=ask_llm(prompt)
    print('\nLLM Response:')
    print(answer)