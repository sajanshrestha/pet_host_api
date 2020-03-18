from flask_restful import Resource, reqparse
from host import hosts
from database import Database


class OwnerRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username', required=True, type=str)
    parser.add_argument('password', required=True, type=str)

    def post(self):
        data = OwnerRegister.parser.parse_args()

        Database.create_owner(data['username'], data['password'])
        return {'message': 'owner created'}, 201


class HostRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username', required=True, type=str)
    parser.add_argument('password', required=True, type=str)

    def post(self):
        data = HostRegister.parser.parse_args()

        Database.create_host(data['username'], data['password'])
        return {'message': 'host created'}, 201
