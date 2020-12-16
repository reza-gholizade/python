from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

# set path to env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Set configuration vars from .env file."""

    # Load in enviornemnt variables
    db_host = os.getenv('host')
    db_password = os.getenv('password')
    db_user = os.getenv('username')
    db_name = os.getenv('database')
