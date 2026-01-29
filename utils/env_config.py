from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def getSettings():
    return Settings() # type: ignore
