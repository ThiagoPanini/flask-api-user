"""
---------------------------------------------------------
                    Resumo do Módulo
---------------------------------------------------------


---------------------------------------------------------
                          FAQ
---------------------------------------------------------
"""

# Importando bibliotecas
from os.path import dirname, isfile, join
import pytest
from dotenv import load_dotenv

# Armazenando path das variáveis de ambiente em .env
_ENV_FILE = join(dirname(__file__), '../.env')

# Lendo variáveis de ambiente
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

# Criando uma fixture que será utilizada no escopo da sessão
# ou seja, a cada execução do comando pytest
@pytest.fixture(scope='session')
def client():
    from apps import create_app
    # Cria uma aplicação a partir da função factory
    flask_app = create_app(config_name='testing')

    # O Flask fornece um caminho para testar a aplicação
    # utilizando o Werkzeug test Client
    # e manipulando o contexto
    testing_client = flask_app.test_client()

    # Antes de executar os testes, é criado um contexto com
    # as configurações da aplicação
    ctx = flask_app.app_context()
    ctx.push()

    # Retorna o client criado
    yield testing_client # É aqui onde o teste acontece

    # Remove o contexto ao terminar os testes
    ctx.pop()