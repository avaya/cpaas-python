# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.number
~~~~~~~~~~~~~~~~~~~
Module containing `Number` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Number(BaseNode):

    _allowedContentClass = ()

    def __init__(self, number, sendDigits=None):
        if number is None:
            raise TypeError
        self._value = number
        self.sendDigits = sendDigits
        self._content = None

    @property
    def number(self):
        return self._value

    @number.setter
    def number(self, value):
        if value is None:
            raise TypeError
        self._value = value
