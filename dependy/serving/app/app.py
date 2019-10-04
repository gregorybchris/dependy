from flask import Flask

from dependy.core import settings

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Dependy"

def run(host='localhost', port=8080, debug=0):
    app.run(host=host, port=port)

if __name__ == "__main__":
    run(port=settings.FLASK_RUN_PORT, debug=settings.FLASK_DEBUG)
