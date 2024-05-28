from library.database.db_setup import DatabaseSessionManager
from env import database_config

db_interface = DatabaseSessionManager(database_config)


@db_interface.session_decorator
def create_user(body): ...
