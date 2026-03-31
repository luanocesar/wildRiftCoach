from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    # O Pydantic vai procurar exatamente esses nomes no seu .env
    GROQ_API_KEY: str
    GOOGLE_API_KEY: str
    PROJECT_NAME: str = "Meu Projeto IA" # Com valor padrão se não existir no .env
    MAX_TOKENS: int = 100               # Já converte automaticamente para inteiro
    MODEL_CHAT: str
    MODEL_RAG: str
    
    # Configuração para ler o arquivo
    model_config = SettingsConfigDict(env_file=".env")