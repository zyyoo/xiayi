"""
@ Author : zdoubley 
@ Date : 2020/7/11
@ Usage: 
"""


class BaseResponse(object):
    def __init__(self):
        self.code = 200
        self.msg = 'ok'
        self.data = []

    def dict(self):
        return self.__dict__
