from typing import Self
from pymongo import MongoClient

from os import getenv
from dotenv import load_dotenv


load_dotenv()

class MongoDBConnectionHandler:
    """ Connect to principal database MongoDB """

    def __init__(self, database: str, collection: str) -> None:
        self._connection_string = getenv("DB_URI")
        self._database = database
        self._collection = collection
        self._client = None
        self.connection = None

    def connection_db(self) -> None:
        """ Connect to database """

        if not self._connection_string:
            raise Exception("Set the DB_URI environment variable")

        self._client = MongoClient(self._connection_string)
        database = self._client[self._database]
        self.connection = database[self._collection]

    def __enter__(self) -> Self:
        """ Connect to database and return class context """

        self.connection_db()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ disconnect database connection """

        self._client.close()
        self.connection = None
