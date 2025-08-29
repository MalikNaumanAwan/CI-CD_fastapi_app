from pydantic_settings import BaseSettings
from pydantic import AnyUrl


class Settings(BaseSettings):
    APP_NAME: str = "fastapi-ci-demo"
    API_PREFIX: str = "/api"
    DATABASE_URL: AnyUrl = "postgresql+asyncpg://postgres:q123@localhost:5432/ci_demo"
    CORS_ORIGINS: list[str] = ["*"]


class Config:
    env_file = ".env"
    case_sensitive = True


settings = Settings()
