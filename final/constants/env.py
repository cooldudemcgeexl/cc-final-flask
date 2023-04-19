import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).parents[1] / '.env'
load_dotenv(ENV_PATH.absolute())

POSTGRES_PWD = os.getenv('POSTGRES_PWD')
