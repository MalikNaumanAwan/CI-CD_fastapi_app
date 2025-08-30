from pydantic_settings import BaseSettings
from pydantic import AnyUrl


class Settings(BaseSettings):
    APP_NAME: str = "fastapi-ci-demo"
    API_PREFIX: str = "/api"
    DATABASE_URL: AnyUrl = (
        "postgresql://neondb_owner:npg_z3pGAn5WPvKw@ep-winter-lab-ady4yz5q-pooler.c-2.us-east-1.aws.neon.tech/demo_ci?sslmode=require&channel_binding=require"
        # "postgresql+asyncpg://postgres:q123@localhost:5432/ci_demo"  # "postgresql+asyncpg://devuser:devpass@db:5432/demo_ci"
    )
    CORS_ORIGINS: list[str] = ["*"]


class Config:
    env_file = ".env"
    case_sensitive = True


settings = Settings()
