# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.mms
~~~~~~~~~~~~~~~~~~~
Module containing `Mms` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Mms(BaseNode):

    _allowedContentClass = ()

    def __init__(
            self,
            mediaUrl,
            to=None,
            from_=None,
            text=None,
            action=None,
            method=None,
            statusCallback=None):
        if mediaUrl is None:
            raise TypeError
        self._value = text
        self.to = to
        self.from_ = from_
        self.action = action
        self.method = method
        self.statusCallback = statusCallback
        self.mediaUrl = mediaUrl
        self._content = []

    @property
    def text(self):
        return self._value

    @text.setter
    def text(self, value):
        if value is None:
            raise TypeError
        self._value = value
