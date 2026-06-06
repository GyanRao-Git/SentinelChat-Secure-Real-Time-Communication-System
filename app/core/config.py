from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str
    VERSION: str
    PORT: int
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SC_",
        case_sensitive=True,
        extra="ignore"
    )

class DatabaseSettings(BaseSettings):
    PG_CONNECTION_STRING: str
    PG_PASSWORD:str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        case_sensitive=True,
        extra="ignore"
    )


class AuthSettings(BaseSettings):
    JWT_SECRET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SC_",
        extra="ignore"
    )

app_settings = AppSettings()
db_settings = DatabaseSettings()
auth_settings = AuthSettings()
