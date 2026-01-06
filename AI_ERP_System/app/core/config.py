from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI ERP System"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # Model Paths
    MODEL_PATH: str = "models/"
    DATA_PATH: str = "data/"
    
    class Config:
        case_sensitive = True

settings = Settings()
