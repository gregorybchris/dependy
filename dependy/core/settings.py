import os

# App Settings

FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', 8080)
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 0)

# Storage Settings

DEPENDY_FILES = os.getenv('DEPENDY_FILES', '/tmp/dependy')
