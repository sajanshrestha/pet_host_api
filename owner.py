from flask_restful import Resource, reqparse
from database import Database


class Owners(Resource):
    def get(self):
        owners = Database.get_owners()
        if owners:
            return owners, 200
        else:
            []


class Owner(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=int)
    parser.add_argument('password', type=int)

    def get(self, owner_id):

        owner = Database.get_owner(int(owner_id))
        if owner:
            return owner, 200
        else:
            return {'message': 'owner not found'}, 404

    def put(self, owner_id):
        pass

    def delete(self, owner_id):
        Database.delete_owner(int(owner_id))
        return {'message': 'owner deleted'}
