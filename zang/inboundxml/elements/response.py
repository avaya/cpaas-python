# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.response
~~~~~~~~~~~~~~~~~~~
Module containing `Response` inbound xml element
"""
from zang.inboundxml.elements.constants import XML_DECLARATION

from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.answer import Answer
from zang.inboundxml.elements.record import Record
from zang.inboundxml.elements.pause import Pause
from zang.inboundxml.elements.redirect import Redirect
from zang.inboundxml.elements.ping import Ping
from zang.inboundxml.elements.sms import Sms
from zang.inboundxml.elements.mms import Mms
from zang.inboundxml.elements.play_last_recording import PlayLastRecording
from zang.inboundxml.elements.reject import Reject
from zang.inboundxml.elements.dial import Dial
from zang.inboundxml.elements.hangup import Hangup
from zang.inboundxml.elements.say import Say
from zang.inboundxml.elements.play import Play
from zang.inboundxml.elements.gather import Gather


class Response(BaseNode):

    _allowedContentClass = (
        Answer,
        Record,
        Pause,
        Redirect,
        Ping,
        Sms,
        Mms,
        PlayLastRecording,
        Reject,
        Dial,
        Hangup,
        Say,
        Play,
        Gather,
    )

    def __init__(
            self,
            statusCallback=None,
            statusMethod=None,
            heartbeatCallback=None,
            heartbeatMethod=None,
    ):
        self.statusCallback = statusCallback
        self.statusMethod = statusMethod
        self.heartbeatCallback = heartbeatCallback
        self.heartbeatMethod = heartbeatMethod
        self._content = []
        self._value = None

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

    @property
    def xml(self):
        """
        Create a xml element with corresponding attributes and child elements.

        :rtype: str
        """
        s = XML_DECLARATION + super(Response, self).xml
        return s
