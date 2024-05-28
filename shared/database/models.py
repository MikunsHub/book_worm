from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import BOOLEAN, INTEGER, TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(INTEGER, primary_key=True, index=True)
    email = Column(VARCHAR, unique=True, nullable=False)
    password = Column(VARCHAR, nullable=False)
    firstname = Column(VARCHAR, nullable=False)
    lastname = Column(VARCHAR, nullable=False)
    is_active = Column(BOOLEAN, default=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    updated_at = Column(TIMESTAMP, server_default=text("now()"))
