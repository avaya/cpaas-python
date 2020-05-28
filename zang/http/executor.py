# -*- coding: utf-8 -*-

"""
zang.http.executor
~~~~~~~~~~~~~~~~~~~
This module contains a default http executor.
"""

import base64
import json
import requests
import sys

from zang.helpers.helpers import is_collection
from zang.domain.account import Account
from zang.exceptions.zang_exception import ZangException

if sys.version_info >= (3, 0):
    from urllib.parse import urlencode
    str_classes = (str, bytes)
else:
    from urllib.parse import urlencode


class Executor(object):
    """Creates a default http executor"""

    def __init__(self, configuration=None, session=None):
        if session is None:
            session = requests.session()

        self._configuration = configuration
        self._session = session

    @property
    def configuration(self):
        return self._configuration

    def create(self, resource, class_, data):
        return self._setResource(resource, class_, data)

    def read(self, resource, class_, params=None):
        return self._getResource(resource, class_, params=params)

    def update(self, resource, class_, data=None):
        return self._setResource(resource, class_, data)

    def delete(self, resource, class_):
        return self._deleteResource(resource, class_)

    @staticmethod
    def _resource_serialize(o):
        """Returns JSON serialization of given object."""
        return json.dumps(o)

    @staticmethod
    def _resource_deserialize(s):
        """Returns dict deserialization of a given JSON string."""
        try:
            js = json.loads(s)
            return js
        except ValueError:
            raise ZangException('The API Response was not valid.')

    def _httpResource(self, method, url, params=None, data=None):
        """Makes an HTTP request."""

        headers = self._headers()
        if method == 'POST':
            headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        # print('url', url)
        # print('data', data)
        # print('params', params)
        # print('headers', headers)

        r = self._session.request(
            method, url, params=params, headers=headers, data=data)

        try:
            r.raise_for_status()
        except Exception as e:
            raise ZangException(e)
        return r

    def _headers(self):
        accountSid = self._configuration.sid
        authToken = self._configuration.authToken

        headers = {}
        usrPass = accountSid + ':' + authToken
        if sys.version_info >= (3, 0):
            usrPass = str.encode(usrPass)
        base64_ = base64.b64encode(usrPass).decode('utf-8')
        headers.update({'Authorization': 'Basic %s' % base64_})
        return headers

    def _url(self, resource, class_):
        accountSid = self._configuration.sid
        baseUlr = self._configuration.baseUrl

        if not is_collection(resource):
            resource = [resource]

        if class_ is not Account:
            resource = ('Accounts', accountSid) + resource

        args = map(str, resource)
        url = ('/'.join([baseUlr] + list(args))) + '.json'
        return url

    def _getResource(self, resource, class_, params=None):
        url = self._url(resource, class_)
        response = self._httpResource('GET', url, params=params)
        return self._newFromResponse(response, class_)

    def _setResource(self, resource, class_, data):
        if not isinstance(data, str_classes):
            try:
                data = urlencode(data)
            except Exception:
                pass
        url = self._url(resource, class_)
        response = self._httpResource('POST', url, data=data)
        return self._newFromResponse(response, class_)

    def _deleteResource(self, resource, class_):
        url = self._url(resource, class_)
        response = self._httpResource('DELETE', url)
        return self._newFromResponse(response, class_)

    def _newFromResponse(self, response, class_):
        json_ = self._resource_deserialize(response.content.decode('utf-8'))
        # print(json.dumps(json_, indent=4, sort_keys=True))
        return class_.new_from_dict(json_)
