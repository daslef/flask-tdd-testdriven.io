from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

from project.api.users.models import User

from project.api.users.services import (
    get_all_users,
    get_user_by_email,
    add_user,
    get_user_by_id,
    update_user,
    delete_user,
)

users_namespace = Namespace("users")

user = user_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)


class UsersList(Resource):
    @user_namespace.marshal_with(user, as_list=True)
    def get(self):
        return get_all_users(), 200

    @user_namespace.expect(user, validate=True)
    def post(self):
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_email(email)
        if user:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        add_user(username, email)
        response_object = {"message": f"{email} was added!"}
        return response_object, 201


class Users(Resource):
    @user_namespace.marshal_with(user)
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if not user:
            user_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200

    def delete(self, user_id):
        response_object = {}
        user = get_user_by_id(user_id)
        if not user:
            user_namespace.abort(404, f"User {user_id} does not exist")
        delete_user(user)
        response_object["message"] = f"{user.email} was removed!"
        return response_object, 200

    @user_namespace.expect(user, validate=True)
    def put(self, user_id):
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_id(id)
        if not user:
            user_namespace.abort(404, f"User {user_id} does not exist")
        update_user(user, username, email)
        response_object["message"] = f"{user.id} was updated!"
        return response_object, 200


user_namespace.add_resource(UsersList, "")
user_namespace.add_resource(Users, "/<int:user_id>")
