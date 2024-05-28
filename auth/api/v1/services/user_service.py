import bcrypt
from api.v1.queries import add_user, get_user


def create_user(body):
	req_data = body.model_dump()

	existing_user = get_user(req_data['email'])

	if existing_user:
		raise ValueError('User with this email already exists')

	hashed_password = bcrypt.hashpw(req_data['password1'].encode('utf-8'), bcrypt.gensalt())
	req_data['password'] = hashed_password.decode('utf-8')

	new_user = add_user(req_data)
	return new_user
