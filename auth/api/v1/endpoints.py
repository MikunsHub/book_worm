from flask import Blueprint
from flask_pydantic import validate

from api.v1.models import UserCreateModel, UserResponseModel
from api.v1.services.user_service import create_user
from api.v1.decorators import serialize_response


v1 = Blueprint('v1', __name__)


@v1.route('/user', methods=['POST'])
@validate()
@serialize_response(UserResponseModel)
def register_user(body: UserCreateModel):
	user_data = create_user(body)
	return user_data


@v1.route('/example', methods=['GET'])
def example():
	return 'This is an example route'
