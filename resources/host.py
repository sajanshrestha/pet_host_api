from flask_restful import Resource
from models.database import Database


class Hosts(Resource):
    def get(self):
        hosts = Database.get_hosts()
        return hosts if hosts else []


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
