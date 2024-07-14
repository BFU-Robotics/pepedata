import os

from dotenv import load_dotenv

PLANKA_URL = os.getenv("PLANKA_URL")
EMAIL = os.getenv("PLANKA_EMAIL")
PASSWORD = os.getenv("PLANKA_PASSWORD")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 60))
DATABASE_URL = os.getenv("DATABASE_URL")
