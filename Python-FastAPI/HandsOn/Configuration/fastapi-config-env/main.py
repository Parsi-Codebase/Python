from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv() # Load environment variables from .env file
app=FastAPI(
    title=os.getenv('APP_NAME', 'Student API'),
    debug=os.getenv('DEBUG', 'False').lower() == 'true'
)
@app.get('/')
async def home():
    return {
        'message':'Student API is running',
        'environment':os.getenv('APP_ENV', 'development')
    }
@app.get('/config')
async def get_config():
    return{
        'app_name':os.getenv('APP_NAME', 'Student API'),
        'environment':os.getenv('APP_ENV', 'development'),
        'debug':os.getenv('DEBUG', 'False').lower() == 'true',
        'database_configured':bool(os.getenv('DATABASE_URL')),
        'secret_configured':bool(os.getenv('SECRET_KEY')),
        'api_key_configured':bool(os.getenv('API_KEY'))
    }