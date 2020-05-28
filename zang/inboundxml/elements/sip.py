# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.sip
~~~~~~~~~~~~~~~~~~~
Module containing `Sip` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Sip(BaseNode):

    _allowedContentClass = ()

    def __init__(self, address, username=None, password=None):
        if address is None:
            raise TypeError
        self._value = address
        self.username = username
        self.password = password
        self._content = None

    @property
    def address(self):
        return self._value

    @address.setter
    def address(self, value):
        if value is None:
            raise TypeError
        self._value = value
