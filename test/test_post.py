import unittest

from wynum import Client
from wynum.exceptions import *

client = Client("a742bc685f072fe624f61ee2119d66982x", "8979947")
data = {
    "name": "groot",
    "height": 5,
    "weight": 42,
    "Details_hobbies": ["painting"],
    "Details_required": "yes",
    "id": "2"
}


class TestClient(unittest.TestCase):
    def test_normal_post(self):
        res = client.postdata(data)
        message = res.get('error')
        self.assertNotEqual(message, "Error while decoding request body.")

    def test_file_post(self):
        client = Client("a742bc685f072fe624f61ee2119d66982x", "6138287")
        with open(__file__) as f:
            data = {"id": "1", "file": f}
            res = client.postdata(data)
            message = res.get('error')
            self.assertNotEqual(message, "Error while decoding request body.")

    def test_normal_update(self):
        res = client.update(data)
        message = res.get('error')
        self.assertNotEqual(message, "Error while decoding request body.")

    def test_file_update(self):
        client = Client("a742bc685f072fe624f61ee2119d66982x", "6138287")
        with open(__file__) as f:
            data = {"id": "1", "file": f}
            res = client.update(data)
            message = res.get('error')
            self.assertNotEqual(message, "Error while decoding request body.")

    def test_get_data(self):
        try:
            res = client.getdata()
            self.assertIs(type(res), list)
        except Exception:
            self.fail("getdata() failed unexpectedly!")

    def test_get_schema(self):
        try:
            res = client.getschema()
            self.assertIs(type(res), list)
        except Exception:
            self.fail("getschema() failed unexpectedly!")

    def test_if_raises_auth_exception(self):
        client = Client("a742bc685f072fe624f61ee2119d66982", "8979947")
        with self.assertRaises(AuthException):
            client.postdata(data)

        with self.assertRaises(AuthException):
            client.getdata()

        with self.assertRaises(AuthException):
            client.getschema()

        with self.assertRaises(AuthException):
            client.update(data)

    def test_if_raises_invalid_token_exception(self):
        client = Client("a742bc685f072fe624f61ee2119d66982x", "897994")
        with self.assertRaises(InvalidTokenException):
            client.postdata(data)

        with self.assertRaises(InvalidTokenException):
            client.getdata()

        with self.assertRaises(InvalidTokenException):
            client.getschema()

        with self.assertRaises(InvalidTokenException):
            client.update(data)
