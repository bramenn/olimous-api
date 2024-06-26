from os import getenv

from dotenv import load_dotenv

load_dotenv()

POSTGRES_URI = getenv("POSTGRES_URI")
MAX_TICKET_BY_VIEWER = getenv("MAX_TICKET_BY_VIEWER")
DEFAUL_FREE_LIMIT_VIEWERS = getenv("DEFAUL_FREE_LIMIT_VIEWERS")
DEFAUL_FREE_LIMIT_PARTICIPANTS = getenv("DEFAUL_FREE_LIMIT_PARTICIPANTS")
