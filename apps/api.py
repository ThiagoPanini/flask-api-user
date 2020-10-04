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

# Importando bibliotecas
from application import app

# Definindo rotas de acordo com a sintaxe do flask
@app.route('/')
def index():
    return {'hello': 'World Hiro'}
