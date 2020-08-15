from pydantic import BaseSettings
from dotenv import load_dotenv
import logging
import os

load_dotenv(dotenv_path=f'{os.getenv("HOME")}/.openapi/.env')

class Settings(BaseSettings):
    serving_management_url:str = "http://torch:3002"
    serving_inference_url:str = "http://torch:3003"
    openai_completion_url:str = 'https://api.openai.com/v1/engines/davinci/completions'
    openai_secret_key:str = os.getenv("OPENAI_API_SECRET","")
    logging_level = logging.DEBUG

settings = Settings()

logger = logging.getLogger(__name__)
logger.setLevel(level=settings.logging_level)
