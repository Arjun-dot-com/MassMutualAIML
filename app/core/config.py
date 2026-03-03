from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Metadata
    PROJECT_NAME: str = "AI Personalized Learning Service"
    PROJECT_VERSION: str = "1.0.0"
    
    # API Keys
    GROQ_API_KEY: str

    # This tells Pydantic to read from the .env file in your root folder
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Create a global instance of the settings to import everywhere else
settings = Settings()