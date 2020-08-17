import flask
import os
from dotenv import dotenv_values

# Load environment variables
# Flask will autoload variables from .env file when using
# `flask run` command or running the `app.py` file
config_dict = dotenv_values()
app = flask.Flask(__name__)

app.config.from_mapping(config_dict)

# Weird circular imports going on here
# but we must import routes **AFTER** we create
# the app variable or else there will be a great
# many errors
import routes

if __name__ == '__main__':
    app.run(debug=True)
