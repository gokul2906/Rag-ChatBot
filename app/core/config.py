import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    ENV: str = os.getenv("ENV", "development")
    APP_NAME: str = os.getenv("APP_NAME", "RAG")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()