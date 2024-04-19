from os import getenv

from dotenv import load_dotenv

load_dotenv()

POSTGRES_URI = getenv("POSTGRES_URI")
