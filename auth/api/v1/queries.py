from env import database_config
from sqlalchemy.orm import Session
from library.database.db_setup import DatabaseSessionManager
from library.database.models import User


db_interface = DatabaseSessionManager(database_config)


@db_interface.session_decorator
def get_user(email: str, session: Session):
	user = session.query(User).filter(User.email == email).first()  # type: ignore
	return user


@db_interface.session_decorator
def add_user(req_data, session: Session):
	new_user = User(
		email=req_data['email'],
		password=req_data['password'],
		firstname=req_data['firstname'],
		lastname=req_data['lastname'],
	)
	session.add(new_user)
	return new_user.to_dict()
