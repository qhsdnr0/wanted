import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    WANTED_USER : str = os.getenv("WANTED_USER")
    WANTED_PASSWORD = os.getenv("WANTED_PASSWORD")
    WANTED_HOST : str = os.getenv("WANTED_HOST","localhost")
    WANTED_PORT : str = os.getenv("WANTED_PORT",5432) # default WANTED port is 5432
    WANTED_NAME : str = os.getenv("WANTED_NAME","tdd")
    DATABASE_URL = f"mysql://{WANTED_USER}:{WANTED_PASSWORD}@{WANTED_HOST}:{WANTED_PORT}/{WANTED_NAME}"

settings = Settings()