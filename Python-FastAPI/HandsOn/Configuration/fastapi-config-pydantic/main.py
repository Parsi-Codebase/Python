from fastapi import FastAPI
from core.config import settings
app=FastAPI(
    title=settings.app_name,
    debug=settings.debug
)
@app.get('/')
async def home():
    return {
        'message':'Student API is running',
        'environment':settings.app_env
    }
@app.get('/config')
async def get_config():
    return{
        'app_name':settings.app_name,
        'environment':settings.app_env,
        'debug':settings.debug,
        'database_configured':bool(settings.database_url),
        'secret_configured':bool(settings.secret_key),
        'api_key_configured':bool(settings.api_key)
    }