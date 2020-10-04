"""
-----------------------------
Perguntas sobre este arquivo:
-----------------------------

1. Qual o objetivo do script setup.py?
    1.1 Qual sua usabilidade em aplicações criadas?
    1.2 Como se dá seu consumo na prática?

2. Quais são as informações necessárias a serem preenchidas?

3. Qual o papel do "double underscore __" no nome das variáveis?
"""

# Third
from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api Python Flask'
__long_description__ = 'This is an API to Flask Api Users'

__author__ = 'Thiago Panini'
__author_email__ = 'thipanini94@gmail.com'

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
)