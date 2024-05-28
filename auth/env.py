import os

from library.database.db_setup import DatabaseConfig

PG_USER = os.environ['PG_USER']
PG_PASSWORD = os.environ['PG_PASSWORD']
PG_HOST = os.environ['PG_HOST']
PG_NAME = os.environ['PG_NAME']
PG_PORT = os.environ['PG_PORT']


DATABASE_DRIVER = 'postgresql'

database_config = DatabaseConfig(
	drivername=DATABASE_DRIVER,
	username=PG_USER,
	password=PG_PASSWORD,
	host=PG_HOST,
	database=PG_NAME,
	port=PG_PORT,
)
