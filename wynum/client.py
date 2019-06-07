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

    def getdata(self, **kwargs):
        kwargs = self.__validate_and_parse_args(kwargs)
        response = requests.get(self.__data_url, params=kwargs)
        return response.json()

    def update(self, data):
        response = requests.put(self.__data_url, data=json.dumps(data))
        return response.json()

    def postdata(self, data):
        response = requests.post(self.__data_url, data=json.dumps(data))
        return response.json()

    def __validate_data(self, data, schema):
        raise NotImplementedError
    
    def __validate_and_parse_args(self, args):
        if (args.get('ids')):
            args['ids'] = ','.join([str(i) for i in args['ids']])

        if (args.get('order_by')):
            if not (args['order_by'] in ['asc', 'desc'] and type(args['order_by'] == 'str')):
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
