# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.say
~~~~~~~~~~~~~~~~~~~
Module containing `Say` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Say(BaseNode):

    _allowedContentClass = ()

    def __init__(self, text, voice=None, language=None, loop=None):
        if text is None:
            raise TypeError
        self._value = text
        self.voice = voice
        self.language = language
        self.loop = loop
        self._content = None

    @property
    def text(self):
        return self._value

    @text.setter
    def text(self, value):
        if value is None:
            raise TypeError
        self._value = value
