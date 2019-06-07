import json

import requests
from . import schema


class Client(object):
    WYNNUM_BASE_URL = "https://api.wynum.com"
    SCHEMA_BASE_URL = "{}/{}".format(WYNNUM_BASE_URL, 'component')
    DATA_BASE_URL = "{}/{}".format(WYNNUM_BASE_URL, 'data')

    def __init__(self, secret, token):
        self.__secret = secret
        self.__token = token
        self.__schema_url = "{}/{}?secret_key={}".format(
            self.SCHEMA_BASE_URL, token, secret)
        self.__data_url = "{}/{}?secret_key={}".format(
            self.DATA_BASE_URL, token, secret)
        self.identifier = None
        self.schema = None

    def getschema(self):
        response = requests.get(self.__schema_url)
        schema_json_list = response.json()['components']
        schemas = [schema.Schema(json) for json in schema_json_list]
        self.schema = schemas
        self.identifier = response.json()['identifer']
        return schemas

    def getdata(self):
        raise NotImplementedError

    def update(self, data):
        response = requests.put(self.__data_url, data=json.dumps(data))
        return response.json()

    def postdata(self, data):
        response = requests.post(self.__data_url, data=json.dumps(data))
        return response.json()

    def __validate_data(self, data, schema):
        raise NotImplementedError
