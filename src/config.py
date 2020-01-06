import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class FlaskConfig(object):
    SECRET_KEY = os.environ.get("PROJECT_KEY", " ")
    

class AppConfig(object):
    PORT = os.environ.get('PORT', 5000)