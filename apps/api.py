# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

# Creating class using Resource
class Index(Resource):

    # Defining get operation from http procotol
    def get(self):
        # Returning a simple dictionary (to be transformer automatically on json by flask)
        return {'hello': 'world by apps'}

# Initializint FlaskRestful Api
api = Api()

def configure_api(app):
    
    # Adding resource on '/' route
    api.add_resource(Index, '/')

    # Initializing api with flask configuration
    api.init_app(app)