import requests
OLLAMA_URL='http://localhost:11434/api/chat'
MODEL_NAME='phi3'
def ask_llm(prompt:str)->None:
    payload={
        'model':MODEL_NAME,
        'messages':[
            {
                'role':'user',
                'content':prompt
            },   
        ],
        'stream':True
    }
    with requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300,
        stream=True
    ) as response:
        response.raise_for_status() # reads the incoming json lines
        print('\nLLM Response:')
        for line in response.iter_lines():
            if line:
                chunk=requests.models.complexjson.loads(line)
                # extract generated text from each chunk
                content=chunk.get('message',{}).get('content','')
                print(content,end='',flush=True) #flush=True: Display each chunk immediately
                if chunk.get('done'): # Detects the final response chunk
                    break
    
   
    print()
    
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    answer = ask_llm(prompt)