from functools import wraps
from typing import NamedTuple
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from contextlib import contextmanager


class DatabaseConfig(NamedTuple):
    drivername: str
    username: str
    password: str
    host: str
    database: str
    port: str


class DatabaseSessionManager:
    def __init__(self, db_config: DatabaseConfig):
        self.url = URL.create(**db_config._asdict())
        try:
            self.engine = create_engine(self.url)
        except Exception as e:
            raise RuntimeError(f"Connection failed: {e}") from e
        self.SessionLocal = sessionmaker(bind=self.engine)

    @contextmanager
    def in_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def session_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self.in_session() as session:
                kwargs['session'] = session
                return func(*args, **kwargs)
        return wrapper
