from collections.abc import Generator
from threading import Lock
import ollama
from fastapi import FastAPI,HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel,Field

# Configuration
MODEL_NAME='phi3'
SYSTEM_PROMPT=(
    "You are a helpful AI assistant. "
    "Provide clear and accurate answers."
)
app=FastAPI(
    title='Ollama Chat API',
    description='Chat with a local LLM using Ollama and Fast API',
    version='1.0.0'
)
# In-memory conversation history
conversations:dict[str,list[dict[str,str]]]={}
history_lock=Lock()
#Request model
class ChatRequest(BaseModel):
    prompt:str=Field(min_length=1,max_length=10000)
    session_id:str=Field(default='default',min_length=1,max_length=100)
#Response model
class ChatResponse(BaseModel):
    session_id:str
    model:str
    response:str
def get_messages(session_id:str)->list[dict[str,str]]:
    '''Get or create the conversation history'''
    with history_lock:
        if session_id not in conversations:
            conversations[session_id]=[
                {
                    'role':'system',
                    'content':SYSTEM_PROMPT
                }
            ]
        return list(conversations[session_id])
def add_message(session_id:str,role:str,content:str)->None:
    '''Add a message to conversation history.'''
    with history_lock:
        conversations[session_id].append({
            'role':role,
            'content':content
        })
def remove_last_message(session_id:str)->None:
    '''Remove an unanswered user prompt after an API failure'''
    with history_lock:
        if(
            session_id in conversations
            and conversations[session_id][-1]['role']=='user'
        ):
            conversations[session_id].pop()
@app.get('/')
def home():
    return {
        'message':"Ollama Chat API is running",
        'model':MODEL_NAME,
        'docs':'/docs'
    }
@app.get('/health')
def health():
    '''Check whether Ollama is reachable and the model is available'''
    try:
        models=ollama.list()
        available_models=[
            model.model for model in models.models
        ]
        model_available=any(
            name.split(':')[0]==models
            for name in available_models
        )
        return{
            'api':'running',
            'ollama':'connected',
            'model':MODEL_NAME,
            'model_available':model_available
        }
    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail=f'Cannot connect to Ollama: {error}'
        ) from error
@app.post('/chat',response_model=ChatResponse)
def chat(request:ChatRequest):
    '''Generate a complete response and preserve conversation history'''
    messages=get_messages(request.session_id)
    # Save the current user message
    add_message(
        request.session_id,
        'user',
        request.prompt
    )
    # Include the current prompt in the model request
    messages.append({
        'role':'user',
        'content':request.prompt
    })
    try:
        result=ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=False
        )
        answer=result.message.content or ''
        add_message(
            request.session_id,
            'assistant',
            answer
        )
        return ChatResponse(
            session_id=request.session_id,
            model=MODEL_NAME,
            response=answer
        )
    except Exception as error:
        remove_last_message(request.session_id)
        raise HTTPException(
            status_code=502,
            detail=f'Ollama chat failed: {error}'
        ) from error

@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    messages = get_messages(request.session_id)

    messages.append({
        "role": "user",
        "content": request.prompt
    })

    def generate():
        answer = ""

        try:
            # Request a streaming response from Ollama
            stream = ollama.chat(
                model=MODEL_NAME,
                messages=messages,
                stream=True
            )

            for chunk in stream:
                content = chunk.message.content or ""

                if content:
                    answer += content
                    yield content

            # Save conversation only after successful completion
            add_message(
                request.session_id,
                "user",
                request.prompt
            )

            add_message(
                request.session_id,
                "assistant",
                answer
            )

        except Exception as error:
            print(f"Ollama streaming error: {error}")
            yield f"\nError: {error}"

    return StreamingResponse(
        generate(),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )

@app.delete('/chat/{session_id}')
def clear_conversation(session_id:str):
    '''Clear a session's history'''
    with history_lock:
        conversations.pop(session_id,None)
    return{
        'message':'Conversation history cleared',
        'session_id':session_id
    }