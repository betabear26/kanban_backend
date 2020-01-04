import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("PROJECT_KEY", " ")