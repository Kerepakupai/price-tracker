import os
from dotenv import load_dotenv

load_dotenv("./.env")


EMAIL_ACCOUNT = os.environ["EMAIL_ACCOUNT"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
