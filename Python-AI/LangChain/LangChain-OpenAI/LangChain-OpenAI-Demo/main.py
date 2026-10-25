from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0.3,
    api_key=os.getenv('OPENAI_API_KEY')
)
response=model.invoke('Who is India PM,short answer')
print(response.content)