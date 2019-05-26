import json
import requests


class Client(object):
    WYNNUM_BASE_URL = "https://api.wynum.com"
    SCHEMA_BASE_URL = "{}/{}".format(WYNNUM_BASE_URL, 'component')
    DATA_BASE_URL = "{}/{}".format(WYNNUM_BASE_URL, 'data')

    def __init__(self, secret, token):
        self.__secret = secret
        self.__token = token
        self.__schema_url = "{}/{}".format(self.SCHEMA_BASE_URL, token)
        self.__data_url = "{}/{}".format(self.DATA_BASE_URL, token)
    
    def getschema(self):
        response = requests.get(self.__schema_url)
        return response.json()
    
    def getdata(self):
        raise NotImplementedError
    
    def postdata(self, data):
        response = requests.post(self.__data_url, data=json.dumps(data))
        return response.json()

    def __validate_data(self, data, schema):
        raise NotImplementedError

    def __parse_schema(self, schema_json):
        raise NotImplementedError