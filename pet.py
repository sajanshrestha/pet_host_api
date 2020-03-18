from flask_restful import Resource


pets = [
    {
        'id': 1,
        'name': 'Captain',
        'breed': 'Pitbull',
        'color': 'Brindle',
        'owner_id': 1
    },
    {
        'id': 2,
        'name': 'Momo',
        'breed': 'French Bulldog',
        'color': 'Mix',
        'owner_id': 2
    }
]


class Pets(Resource):
    def get(self):
        return pets, 200
