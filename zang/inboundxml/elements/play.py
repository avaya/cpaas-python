# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.play
~~~~~~~~~~~~~~~~~~~
Module containing `Play` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Play(BaseNode):

    _allowedContentClass = ()

    def __init__(self, url, loop=None):
        if url is None:
            raise TypeError
        self._value = url
        self.loop = loop
        self._content = None

    @property
    def url(self):
        return self._value

    @url.setter
    def url(self, value):
        if value is None:
            raise TypeError
        self._value = value
