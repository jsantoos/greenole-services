from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    DISCORD_WEBHOOK_URL: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
