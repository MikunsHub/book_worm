from pydantic import BaseModel


class UserCreateModel(BaseModel):
	email: str
	password1: str
	password2: str
	firstname: str
	lastname: str


class UserResponseModel(BaseModel):
	email: str
	firstname: str
	lastname: str

	class Config:
		from_attributes = True
