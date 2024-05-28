from functools import wraps
from flask import jsonify


def serialize_response(model):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			response = f(*args, **kwargs)
			return jsonify(model.from_orm(response).dict())

		return decorated_function

	return decorator
