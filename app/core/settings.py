import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mistral_api_key: str = os.getenv("MISTRAL_API_KEY", "")

settings = Settings()
