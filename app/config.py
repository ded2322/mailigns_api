from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    REDIS_PORT: str
    REDIS_HOST: int

    HOST_SMTP:str
    PORT_SMTP:int
    EMAIL_SENDER:str
    PASSWORD:str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="app/env")


try:
    settings = Settings()
except Exception as e:
    print(f"Ошибка при инициализации настроек: {e}")
