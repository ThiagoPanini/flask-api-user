"""
-----------------------------
Perguntas sobre este arquivo:
-----------------------------

1. Como funciona o módulo getenv da biblioteca os?
    R: https://docs.python.org/3/library/os.html

2. Qual a usabilidade do arquivo config.py?
    R: https://www.geeksforgeeks.org/python-os-getenv-method/

3. Por que são criadas duas classes (Config e DevelopmentConfig(Config))

4. Em um teste simples, os retornos da função getenv() são nulos pras chaves 'SECRET KEY', 'APP_PORT' e 'DEBUG'. Como contornar?
    R: Na verdade, os.getenv(key) é um método que simplesmente busca os valores das variáveis de ambientes passadas no argumento "key"
        - Se essa variável não existe, None é retornado
        - É possível passar uma alternativa dentro do argumento "default" do método getenv()

5. Como são setadas as variáveis de ambiente antes de serem coletadas pelo os.getenv(key)?
    R: Ao longo do desenvolvimento da aplicação, o arquivo .env (localizado na raíz do diretório do projeto) será populado com as informações relavantes
    dentro das variáveis de ambiente sensíveis ao os.getenv(key)
    * O pacote python-dotenv é o responsável por permitir a leitura das variáveis de ambiente automaticamente no arquivo application.py
"""

# Python
from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY') or '8QAzMJCmwETRvGKBxoZw'
    APP_PORT = int(getenv('APP_PORT', default=5000))
    DEBUG = getenv('DEBUG', default=True)

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}