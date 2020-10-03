# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv
from apps import create_app

# Adding .env file to path
_ENV_FILE = join(dirname(__file__), '.env')

# Using dotenv for loading file
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Instancing factory function already built
app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # Running the flask web server
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )