from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql+asyncpg://postgres:password@db/task_management"
    SQLALCHEMY_SYNC_DATABASE_URL: str = "postgresql://postgres:password@db/task_management"
    SECRET_KEY: str = "D8_GVqQOyLd3sfmrZBsKcBkWisWb33Ks07udT6g2jog"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()