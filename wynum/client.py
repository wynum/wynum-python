import json

import requests
from .schema import Schema
from .auth_exception import AuthException


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
        self.__validate_response(response.json())
        schema_json_list = response.json()['components']
        schemas = [Schema(json) for json in schema_json_list]
        self.schema = schemas
        self.identifier = response.json()['identifer']
        return schemas

    def getdata(self, **kwargs):
        kwargs = self.__validate_and_parse_args(kwargs)
        response = requests.get(self.__data_url, params=kwargs)
        self.__validate_response(response.json())
        return response.json()

    def update(self, data):
        if self.__has_files(data):
            files, data = self.__seperate_files_and_data(data)
            response = requests.put(self.__data_url, files=files, data=data)
        else:
            response = requests.put(self.__data_url, data=data)
        self.__validate_response(response.json())
        return response.json()

    def postdata(self, data):
        if self.__has_files(data):
            files, data = self.__seperate_files_and_data(data)
            response = requests.post(self.__data_url, files=files, data=data)
        else:
            response = requests.post(self.__data_url, data=data)
        self.__validate_response(response.json())
        return response.json()
    
    def __has_files(self, data):
        for _, val in data.items():
            if hasattr(val, 'read'):
                return True
        return False
    
    def __seperate_files_and_data(self, data):
        files = {}
        for key, val in data.copy().items():
            if hasattr(val, 'read'):
                files[key] = val
                data.pop(key)
        return (files, data)
    
    def __validate_data(self, data, schema):
        raise NotImplementedError

    def __validate_and_parse_args(self, args):
        if (args.get('ids')):
            args['ids'] = ','.join([str(i) for i in args['ids']])

        if (args.get('order_by')):
            if not (args['order_by'] in ['asc', 'desc'] and
                    type(args['order_by'] == 'str')):
                raise ValueError("order_by must be 'asc' or 'desc'")
            args['order_by'] = args['order_by'].upper()

        if (args.get('limit')):
            if type(args['limit']) != int:
                raise ValueError('limit must be a non-negative integer')
            if args['limit'] < 0:
                raise ValueError('limit must be a non-negative integer')

        if (args.get('to')):
            if type(args['to']) != int:
                raise ValueError('to must be a non-negative integer')

        if (args.get('start')):
            if type(args['start']) != int:
                raise ValueError('start must be a non-negative integer')

        if (args.get('to') and args.get('start')):
            if (args['to'] < args['start']):
                raise ValueError('to must be greater than start')
            args['from'] = args['start']
            args.pop('start')

        return args

    def __validate_response(self, data):
        if (type(data) == dict):
            if data.get('_error') == True:
                if data['_message'] == 'Secret Key Error':
                    raise AuthException('Secret Key Error')
                elif data['_message'] == 'Not Found':
                    raise Exception('Invalid Token')
