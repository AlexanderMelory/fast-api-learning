from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """
    Настройки проекта
    """

    # Настройки БД
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Настройки приложения
    SECRET_KEY: str
    SIGN_ALGORITHM: str

    # Настройки статики
    IMAGES_DIR: str

    # Настройки Celery
    CELERY_BROKER: str

    class Config(BaseSettings.Config):
        env_file = ".env"
        env_file_encoding = 'utf-8'

    @property
    def DB_URL(self) -> str:
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}' f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
