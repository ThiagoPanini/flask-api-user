"""
---------------------------------------------------------
                    Resumo do Módulo
---------------------------------------------------------
    Arquivo de setup com as principais informações da 
aplicação consolidadas a partir da biblioteca setuptools

---------------------------------------------------------
                          FAQ
---------------------------------------------------------

1. Qual o objetivo do script setup.py?

    R: O arquivo setup.py serve para consolidar algumas 
informações úteis da aplicação e fornecer um informativo 
básico para novos desenvolvedores

---------------------------------------------------------

2. Qual sua usabilidade em aplicações criadas?

    R: Na prática, o arquivo setup.py pode ser utilizado 
para instalação dos pacotes no virtual env de trabalho 

Ref [2.1]: https://stackoverflow.com/questions/1471994/what-is-setup-py
"""

# Importando bibliotecas do módulo
from setuptools import find_packages, setup

# Definindo variáveis de setup
__version__ = '0.1.0'
__description__ = 'Api Python Flask'
__long_description__ = 'This is an API to Flask Api Users'

__author__ = 'Thiago Panini'
__author_email__ = 'thipanini94@gmail.com'

# Definindo informações de teste
testing_extras = [
    'pytest',
    'pytest-cov'
]

# Criando setup
setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/ThiagoPanini/flask-api-user',
    keywords='API, Python, Flask',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrator',
        'Operation System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras
    },
)