from dotenv import load_dotenv
import os

load_dotenv()


class Data:

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
