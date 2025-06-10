from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Bookstore API"
    
    class Config:
        case_sensitive = True

settings = Settings() 