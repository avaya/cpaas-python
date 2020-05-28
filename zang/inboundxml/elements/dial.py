# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.dial
~~~~~~~~~~~~~~~~~~~
Module containing `Dial` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.number import Number
from zang.inboundxml.elements.conference import Conference
from zang.inboundxml.elements.user import User
from zang.inboundxml.elements.sip import Sip

import sys
if sys.version_info > (3, 0):
    str_classes = (str, bytes)


class Dial(BaseNode):

    _allowedContentClass = (
        str,
        int,
        Number,
        Conference,
        User,
        Sip,
    )

    def __init__(
            self,
            number=None,
            action=None,
            method=None,
            timeLimit=None,
            callerId=None,
            hideCallerId=None,
            dialMusic=None,
            callbackUrl=None,
            callbackMethod=None,
            confirmSound=None,
            digitsMatch=None,
            straightToVm=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            forwardedFrom=None,
            ifMachine=None,
            ifMachineUrl=None,
            ifMachineMethod=None,
            record=None,
            recordDirection=None,
            recordCallbackUrl=None):
        self._value = number
        self.action = action
        self.method = method
        self.timeLimit = timeLimit
        self.callerId = callerId
        self.hideCallerId = hideCallerId
        self.dialMusic = dialMusic
        self.callbackUrl = callbackUrl
        self.callbackMethod = callbackMethod
        self.confirmSound = confirmSound
        self.digitsMatch = digitsMatch
        self.straightToVm = straightToVm
        self.heartbeatUrl = heartbeatUrl
        self.heartbeatMethod = heartbeatMethod
        self.forwardedFrom = forwardedFrom
        self.ifMachine = ifMachine
        self.ifMachineUrl = ifMachineUrl
        self.ifMachineMethod = ifMachineMethod
        self.record = record
        self.recordDirection = recordDirection
        self.recordCallbackUrl = recordCallbackUrl

        self._content = []

    @property
    def number(self):
        return self._value

    @number.setter
    def number(self, value):
        if value is None:
            raise TypeError
        self._value = value

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
