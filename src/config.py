from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = None

    RESEND_TOKEN: SecretStr
    JWT_SECRET: SecretStr
    FROM_MAIL: str

    model_config = SettingsConfigDict(env_file=".env")


CONFIG = Settings()
