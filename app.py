from flask import request, url_for
from flask_api import FlaskAPI
from os import environ
from sys import exit
from controllers import Routes
from dal import initDb

app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)

for route in Routes:
    app.register_blueprint(route, url_prefix=f'/api/{route.name}')

initDb(app)

if __name__ == "__main__":
    app.run()