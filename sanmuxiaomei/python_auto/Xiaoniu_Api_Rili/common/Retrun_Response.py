#!/usr/bin/python
# -*- coding: UTF-8 _*_

import json


# class return_response(object):
#     def __int__(self, data):
#         self.data = data

def dict_style(data):
    json_response = json.loads(data)
    return json_response

