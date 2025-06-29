from dotenv import load_dotenv
load_dotenv()

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
HOST = os.getenv("HOST")
