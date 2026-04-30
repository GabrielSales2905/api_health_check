from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_URL: str = "postgresql://usuario:senha@localhost:5432/mission"

settings = Settings()