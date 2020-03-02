from flask_restplus import Api

from project.api.users.views import users_namespace
from project.api.ping import ping_namespace

api = Api(version="1.0", title="Users API")

api.add_namespace(ping_namespace, path='/ping')
api.add_namespace(users_namespace, path='/users')
