from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)

api = Api(app)

class UserResource(Resource):
    def get(self):
        ...

api.add_resource(UserResource,)

if __name__ == '__main__':
    app.run(debug=True)