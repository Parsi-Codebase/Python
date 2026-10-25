from pathlib import Path
from pydantic import BaseModel,Field
# DATA_FILE=Path(__file__).parent/'data'/'products.json'
class Settings(BaseModel):
    openai_api_key:str=Field(default=None)
    chat_model:str=Field(default=None)
    embedding_model:str=Field(default=None)
    products_file:Path=Path(__file__).parent/'data'/'products.json'
    
settings=Settings()
    