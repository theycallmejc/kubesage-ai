from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "KubeSage AI"
    environment: str = "development"
    kubectl_kubeconfig: str | None = None
    openrouter_api_key: str | None = None
    chroma_db_path: str = ".data/chroma"
    prometheus_url: str | None = None
    grafana_url: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
