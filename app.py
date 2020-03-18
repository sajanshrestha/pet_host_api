from flask import Flask, render_template
from flask_restful import Api
from owner import Owners, Owner
from register import OwnerRegister, HostRegister
from host import Hosts, Host
from pet import Pets


app = Flask(__name__)

api = Api(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


# Owner endpoints
api.add_resource(OwnerRegister, '/api/owner/register')
api.add_resource(Owners, '/api/owners')
api.add_resource(Owner, '/api/owners/<owner_id>')

# Host endpoints
api.add_resource(HostRegister, '/api/host/register')
api.add_resource(Hosts, '/api/hosts')
api.add_resource(Host, '/api/hosts/<host_id>')


app.run(debug=True)
