import os

# App Settings

FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', 8080)
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 0)
