"""
---------------------------------------------------------
                    Resumo do Módulo
---------------------------------------------------------


---------------------------------------------------------
                          FAQ
---------------------------------------------------------
"""

# Importando bibliotecas
import json

def test_home_response_hello(client):
    """
    **Given** Luiza está acessando a API,
    **When** ela informa a rota/endpoins `/`,
    **Then** a AP deve responder um objeto com a chave `['hello']`
    **And** seu conteúdo deve ser `world by apps`
    """

    # Realiza uma requisição HTTP do tipo GET para o endpoint /
    response = client.get('/')

    # Utilizamos a função loads do módulo json para retornar um dict
    # Precisamos passar por parâmetro para essa função a resposta
    # retornada pelo servidor através da variável response.data
    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção pela chave 'hello'
    assert data['hello'] == 'World Hiro'