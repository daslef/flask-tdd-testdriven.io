from flask import Blueprint
from flask_restplus import Api, Resource, Namespace

ping_blueprint = Blueprint("ping", __name__)
api = Api(ping_blueprint)

ping_namespace = Namespace("ping")

class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong"}


ping_namespace.add_resource(Ping, "")