from flask import Blueprint, jsonify
from flask_pydantic import validate

from api.v1.models import UserModel
from api.v1.services.user_service import create_user


v1 = Blueprint('v1', __name__)


@v1.route('/user', methods=['POST'])
@validate()
def register_user(body: UserModel):
	# body will be an instance of UserModel, automatically validated
	user_data = body.model_dump()
	create_user()
	# Process user_data as needed
	return jsonify(user_data)


@v1.route('/example', methods=['GET'])
def example():
	return 'This is an example route'
