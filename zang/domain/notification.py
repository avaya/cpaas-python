# -*- coding: utf-8 -*-

"""
zang.domain.notification
~~~~~~~~~~~~~~~~~~~
`Notification` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.log_level import LogLevel


class Notification(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'call_sid',
        'more_info',
        'response_headers',
        'response_body',
        'message_text',
        'request_url',
        'request_variables',
        'api_version',
        'uri',
    ]
    _ints = [
        'error_code',
    ]
    _dates = [
        'date_created',
        'date_updated',
        'message_date',
    ]
    _enums = {
        'log': LogLevel,
        'request_method': HttpMethod,
    }

    def __init__(self):
        super(Notification, self).__init__()

    def __repr__(self):
        return '<Notification at 0x%x>' % (id(self))

    @property
    def sid(self):
        return self._sid

    @property
    def accountSid(self):
        return self._account_sid

    @property
    def callSid(self):
        return self._call_sid

    @property
    def moreInfo(self):
        return self._more_info

    @property
    def responseHeaders(self):
        return self._response_headers

    @property
    def responseBody(self):
        return self._response_body

    @property
    def messageText(self):
        return self._message_text

    @property
    def requestUrl(self):
        return self._request_url

    @property
    def requestVariables(self):
        return self._request_variables

    @property
    def apiVersion(self):
        return self._api_version

    @property
    def uri(self):
        return self._uri

    @property
    def log(self):
        return self._log

    @property
    def errorCode(self):
        return self._error_code

    @property
    def dateCreated(self):
        return self._date_created

    @property
    def dateUpdated(self):
        return self._date_updated

    @property
    def messageDate(self):
        return self._message_date

    @property
    def requestMethod(self):
        return self._request_method
