"""
---------------------------------------------------------
                    Resumo do Módulo
---------------------------------------------------------
    O módulo api.py é responsável por definir as rotas
(resources) da API a partir de uma aplicação já instanciada

---------------------------------------------------------
                          FAQ
---------------------------------------------------------
"""

"""# Importando bibliotecas
from application import app

# Definindo rotas de acordo com a sintaxe do flask
@app.route('/')
def index():
    return {'hello': 'World Hiro'}"""

def associate_resources(app):
    """
    Cria recursos e define rotas para a aplicação

    Parâmetros
    ----------
    :param app: aplicação flask instanciada e configurada

    Retorno
    -------
    Essa função não possui retorno, além das definições intrínsecas dos recursos

    Exemplo
    -------
    # Instanciando aplicação do flask
    app = Flask(__name__)
    create_resources(app)
    """

    # Definição de rota '/'
    @app.route('/')
    def index():
        return {'hello': 'World Hiro'}

    # Definição de rota '/home'
    @app.route('/home')
    def home():
        return {'You are in': 'Home'}