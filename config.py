from os import getenv
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class GlobalConfig(BaseSettings):
    API_V_STR: str = "/api/v1"

    class Config:
        case_sensitive = True

global_settings: GlobalConfig = GlobalConfig()