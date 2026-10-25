from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    app_name:str='Student API'
    app_env:str='development'
    debug:bool=False
    database_url:str
    secret_key:str
    api_key:str
    model_config=SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
settings=Settings()