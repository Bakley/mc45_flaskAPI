import unittest
import json

from werkzeug.datastructures import ContentRange
from werkzeug.wrappers import response

from tests.auth.v2.basecases import TestBaseCase

class AuthenticationTestCase(TestBaseCase):
    """
    Test class for the registration endpoint
    """

    def setUp(self) -> None:
        """
        Method to set up authentication testing database
        """
        TestBaseCase.setUp(self)

    def test_invalid_email_format(self):
        """
        Test user email data correct entry
        """

        res = self.client.post(
            '/auth/v2/signup',
            payload=json.dumps(self.invalid_email),
            content_type='application/json'
        )

        self.assertEqual(res, 400)

    def test_valid_email_format(self):
        """
        Test user email data correct entry
        """

        res = self.client.post(
            '/auth/v2/signup',
            payload=json.dumps(self.valid_email),
            content_type='application/json'
        )

        self.assertEqual(res, 201)

if __name__ == "__main__":
    unittest.main()