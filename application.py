"""
---------------------------------------------------------
                    Resumo do Módulo
---------------------------------------------------------
    O módulo application.py tem por objeto organizar e
executar a aplicação criada de acordo com as definições
estabelecidas nos passos anteriores

---------------------------------------------------------
                          FAQ
---------------------------------------------------------
"""

# Importando bibliotecas
from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv
from apps import create_app

# Caminho para o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')

# Lendo as variáveis de ambiente do arquivo .env
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Inicializando aplicação a partir da função factory construída em apps/__init__.py
# Chave FLASK_ENV setada como 'development' no arquivo .env
app = create_app(getenv('FLASK_ENV') or 'default') 

# Instanciando e rodando aplicação
if __name__ == '__main__':
    # Retornando variáveis da aplicação
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # Inicializando aplicação a partir do flask web server
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )