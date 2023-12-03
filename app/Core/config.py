from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Supabase Config
    database_url: str

    # JWT Config
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
