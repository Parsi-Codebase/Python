from dotenv import load_dotenv
import os
from openai import OpenAI
# load the environment variables from .env
load_dotenv()
# create the open ai client
client=OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)
# send a prompt to the model
response=client.responses.create(
    model='gpt-4.1-nano',
    input='explain gen ai in 10 words'
)
print(response.output_text)