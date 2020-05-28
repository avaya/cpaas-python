# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.answer
~~~~~~~~~~~~~~~~~~~
Module containing `Answer` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Reject(BaseNode):

    _allowedContentClass = ()

    def __init__(self, reason=None):
        self.reason = reason
        self._content = None
        self._value = None
