from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    OPENAI_CHAT_MODEL: str = "gpt-4o"
    OPENAI_EMBED_MODEL: str = "text-embedding-3-small"
    MAX_CONTEXT_TOKENS: int = 6000
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
