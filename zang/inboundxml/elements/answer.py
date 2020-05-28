# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.answer
~~~~~~~~~~~~~~~~~~~
Module containing `Answer` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Answer(BaseNode):

    _allowedContentClass = ()

    def __init__(self):
        self._value = None
        self._content = None
