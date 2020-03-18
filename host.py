from flask_restful import Resource
from database import Database

hosts = [
    {
        'id': 1,
        'username': 'walterwhite',
        'password': '1234'
    },

    {
        'id': 2,
        'username': 'michael',
        'password': '1234'
    }

]


class Hosts(Resource):
    def get(self):
        hosts = Database.get_hosts()
        if hosts:
            return hosts
        else:
            return []


class Host(Resource):

    def get(self, host_id):
        host = Database.get_host(int(host_id))
        if host:
            return host, 200
        else:
            return {'message': 'host not found'}, 404

    def put(self, host_id):
        pass

    def delete(self, host_id):
        Database.delete_host(int(host_id))
        return {'message': 'host deleted'}
