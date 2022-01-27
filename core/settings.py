import os


class Settings:
    DATABASE_URL_SYNC = os.getenv("DATABASE_URL_SYNC")
    DATABASE_URL_ASYNC = os.getenv("DATABASE_URL_ASYNC")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
