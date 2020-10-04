"""
O arquivo application.py será o ponto de entrada para a aplicação e execução do servidor web

-----------------------------
Perguntas sobre este arquivo:
-----------------------------

TODO: Estudar as boas práticas de construção do arquivo application.py
"""

# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv
from apps import create_app

# Creating a variable for storing the .env file
_ENV_FILE = join(dirname(__file__), '.env')

# Using dotenv for loading file
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Initializing factory function already built on __init__.py inside apps/ folder (create_app function)
app = create_app(getenv('FLASK_ENV') or 'default') # FLASK_ENV key set up as 'development' on .env file

if __name__ == '__main__':
    # Retrieving main variables for running the app created from create_app() function
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # Running the flask web server using env variables retrieved above
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )