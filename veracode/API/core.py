import requests
import json
import os
from veracode.API.exceptions import *


class REST(object):
    class response:
        def __init__(self, status_code, data, res):
            self.status_code = status_code
            self.data = data
            self.res = res

    def __init__(self, end_point, api_version):
        self.__username = None
        self.__password = None
        try:
            conf = json.load(open(
                os.path.expanduser('~/.veracode/config.json')))
            self.__username = conf.get('username')
            self.__password = conf.get('password')

        except FileNotFoundError as e:
            raise VeracodeConfigError ((
                'You must configure analysiscenter credentials before using'
                ' the veracode API module.\n\n'
                'To configure run: `python -m veracode.configure`'))

        self.__api_server = 'https://analysiscenter.veracode.com/api/'
        self.__end_point = end_point
        self.__server = '/'.join(map(lambda x: str(x).rstrip('/'),
            [self.__api_server, api_version, self.__end_point]))

    def GET(self, query=None, format='text'):
        res = requests.get(
            self.__server, auth=(self.__username, self.__password), 
            params=query)
        return self.response(res.status_code, getattr(res, format), res)

    def POST(self, data):
        res = requests.post(
            self.__server, auth=(self.__username, self.___password), 
            data=data)
        return self.response(res.status_code, getattr(res, format), res)

    def PUT(self):
        raise VeracodeNotImplemented('PUT not implemented.')

    def PATCH(self):
        raise VeracodeNotImplemented('PATCH not implemented.')

    def DELETE(self):
        raise VeracodeNotImplemented('DELETE not implemented.')
