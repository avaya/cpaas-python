# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements..gather
~~~~~~~~~~~~~~~~~~~
Module containing `Gather` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.say import Say
from zang.inboundxml.elements.play import Play
from zang.inboundxml.elements.pause import Pause
from zang.inboundxml.elements.enums.gather_input import GatherInput


class Gather(BaseNode):

    _allowedContentClass = (
        Say,
        Play,
        Pause,
    )

    def __init__(
            self,
            action=None,
            method=None,
            timeout=None,
            finishOnKey=None,
            numDigits=None,
            input=GatherInput.DTMF,
            hints=None,
            language=None):
        self.action = action
        self.method = method
        self.timeout = timeout
        self.finishOnKey = finishOnKey
        self.numDigits = numDigits
        self.input = input
        self.hints = hints
        self.language = language
        self._value = None
        self._content = []

    @property
    def elements(self):
        return self._content

    def addElement(self, element):
        if isinstance(element, type(self)._allowedContentClass):
            self._content.append(element)
        else:
            raise TypeError('Element not allowed for content model')

    def removeElementAtIndex(self, index):
        del self._content[index]
