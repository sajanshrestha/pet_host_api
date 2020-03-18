from flask_restful import Resource, reqparse
from models.database import Database


class Register:
    parser = reqparse.RequestParser()

    parser.add_argument('username', required=True, type=str)
    parser.add_argument('password', required=True, type=str)


class OwnerRegister(Resource, Register):

    def post(self):
        data = self.parser.parse_args()

        Database.create_owner(data['username'], data['password'])
        return {'message': 'owner created'}, 201


class HostRegister(Resource, Register):

    def post(self):
        data = self.parser.parse_args()

        Database.create_host(data['username'], data['password'])
        return {'message': 'host created'}, 201
