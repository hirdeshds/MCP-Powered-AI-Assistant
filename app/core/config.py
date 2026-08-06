from functools import lru_cache
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    # App
    APP_NAME: str = "MCP-Powered AI Assistant"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Persistence
    DATABASE_URL: str = "sqlite:///./data/db.sqlite3"
    REDIS_URL: Optional[str] = None

    # External APIs / services
    OPENAI_API_KEY: Optional[str] = None
    MODEL: str = "openai/gpt-oss-20b"

    # MCP / Tools
    MCP_HOST: str = "127.0.0.1"
    MCP_PORT: int = 8001

    # Misc
    ALLOWED_HOSTS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    @validator("ALLOWED_HOSTS", pre=True)
    def _assemble_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [h.strip() for h in v.split(",") if h.strip()]
        return v

    @validator("SECRET_KEY")
    def _secret_key_must_be_set(cls, v):
        if not v or v.strip() == "" or v == "changeme":
            raise ValueError("SECRET_KEY must be set in environment or .env file")
        return v


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
