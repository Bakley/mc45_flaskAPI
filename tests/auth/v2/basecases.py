import unittest

from app import create_app
from app.auth.v2.models.db_model import Bball_Db

class TestBaseCase(unittest.TestCase):
    """
    Base testing class
    """

    def setUp(self) -> None:
        """
        Method to set up testing database
        """
        testingApp = create_app('testing')
        testingApp.app_context().push()

        self.client = testingApp.test_client()
        self.client.testing = True

        with testingApp.app_context():
            Bball_Db.init_db(app_config.get('TEST_DATABASE_URI'))
            Bball_Db.build_tables()

        self.invalid_email = {
            "email": "2345678",
            "username" : "Koin",
            "password": "hello@123",
            "confirm_password": "hello@123"
        }

        self.valid_email = {
            "email": "a@b.c",
            "username" : "Koin",
            "password": "hello@123",
            "confirm_password": "hello@123"
        }

    def tearDown(self) -> None:
        """
        Destory the testing database
        """
        pass
