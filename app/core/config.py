from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    PORT: int
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SC_",
        case_sensitive=True
    )


env_settings = Settings()
