# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.hangup
~~~~~~~~~~~~~~~~~~~
Module containing `Hangup` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Hangup(BaseNode):

    _allowedContentClass = ()

    def __init__(self, schedule=None, reason=None):
        self.schedule = schedule
        self.reason = reason

        self._content = None
        self._value = None
