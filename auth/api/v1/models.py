from pydantic import BaseModel


class UserModel(BaseModel):
	email: str
	password1: str
	password2: str
	firstname: str
	lastname: str
