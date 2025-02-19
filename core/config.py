from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Pheidippides API"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "An integration built for telex"
    API_PREFIX: str = "/pheidippides-api"
    

settings = Settings()