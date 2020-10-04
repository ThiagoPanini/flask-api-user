"""
-----------------------------
Perguntas sobre este arquivo:
-----------------------------

1. Qual seu papel na execução da aplicação?
2. Trata-se de uma inicialização básica de API do Flask + setagem de configuração?

[BONUS] Relative imports on python: https://stackoverflow.com/questions/6323860/sibling-package-imports 
"""

# -*- coding: utf-8 -*-

from flask import Flask
from config import config

# Importing function that configures the api
from .api import configure_api

def create_app(config_name):

    # Init a Flask object
    app = Flask('api-users')

    # Applies config file already built (config.py) for api object
    app.config.from_object(config[config_name])

    # Executing function that configures the api (built on api.py)
    configure_api(app)

    return app