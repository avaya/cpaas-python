# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.pause
~~~~~~~~~~~~~~~~~~~
Module containing `Pause` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Pause(BaseNode):

    _allowedContentClass = ()

    def __init__(self, length=None):
        self.length = length

        self._content = None
        self._value = None
