from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()


class Settings:

    password = quote_plus(
        os.getenv("DB_PASSWORD")
    )

    DATABASE_URL = (
        f"postgresql://"
        f"{os.getenv('DB_USER')}:"
        f"{password}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )


settings = Settings()
print("DB_NAME =", repr(os.getenv("DB_NAME")))
print("DB_HOST =", repr(os.getenv("DB_HOST")))
print("DB_USER =", repr(os.getenv("DB_USER")))
print("DATABASE_URL =", settings.DATABASE_URL)