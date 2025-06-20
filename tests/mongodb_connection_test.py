import pytest

from app.models.configs import MongoDBConnectionHandler
from tests.mocks.fake_mongo_client import FakeMongoClient


@pytest.fixture
def mongo_handler():
    "mongo handler fixture"

    return MongoDBConnectionHandler("test_database", "test_collection")


def test_init_set_attributes(mongo_handler):
    """ Test attribute values ​​when instantiating the class """

    assert mongo_handler._database == "test_database"
    assert mongo_handler._collection == "test_collection"

    assert mongo_handler._client is None
    assert mongo_handler.connection is None

def test_set_attribuites_client_and_connection_with_connection_db(mongo_handler):
    """ Tests if the attribute values are not None when the connection_db method is called """

    mongo_handler._connection_string = "mongodb://test"
    mongo_handler.connection_db()

    assert mongo_handler._client is not None
    assert mongo_handler.connection is not None

def test_raises_exception_if_uri(monkeypatch):
    """ Test if execution_error is called when there is no db_uri environment variable """

    monkeypatch.delenv("DB_URI", raising=False)
    mongo_handler = MongoDBConnectionHandler("db", "col")

    with pytest.raises(Exception):
        mongo_handler.connection_db()

def test_context_manager_set_connection_atributes(monkeypatch):
    """ Test if when called, context_manager arrows the class attributes to something other than None """

    monkeypatch.setattr(
        "app.models.configs.mongodb_connection.MongoClient",
        FakeMongoClient
    )
    mongo_handler = MongoDBConnectionHandler("test_database", "test_collection")
    mongo_handler._connection_string = "mongodb://test"

    with mongo_handler as handler:
        assert handler._client is not None
        assert handler.connection is not None