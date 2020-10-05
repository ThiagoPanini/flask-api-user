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

# O `client` é a fixture que criamos dentro do arquivo conftest.py
# e é passada como parâmetro na função para ser utilizada dentro
# do escopo

def test_index_response_200(client):
    # Realiza uma requisição http do tipo get para o endpoint /
    response = client.get('/')

    # Verifica a assertividade do código de resposta da requisição
    # http. Ela deve ser exatamente igual 200 retornando um True
    # para o teste
    assert response.status_code == 200