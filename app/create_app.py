from flask import Flask

# set FLASK_APP=create_app.py
# flask run
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello world123 2+2=4 !"

    return app
