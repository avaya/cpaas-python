# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.ping
~~~~~~~~~~~~~~~~~~~
Module containing `Ping` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Ping(BaseNode):

    _allowedContentClass = ()

    def __init__(self, url, method=None):
        if url is None:
            raise TypeError
        self._value = url
        self.method = method
        self._content = None

    @property
    def url(self):
        return self._value

    @url.setter
    def url(self, value):
        if value is None:
            raise TypeError
        self._value = value
