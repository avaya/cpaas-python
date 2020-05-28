# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.conference
~~~~~~~~~~~~~~~~~~~
Module containing `Conference` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Conference(BaseNode):

    _allowedContentClass = ()

    def __init__(
            self,
            name,
            muted=None,
            beep=None,
            startConferenceOnEnter=None,
            endConferenceOnExit=None,
            maxParticipants=None,
            waitSound=None,
            hangupOnStar=None,
            callbackUrl=None,
            callbackMethod=None,
            digitsMatch=None,
            stayAlone=None,
            record=None,
            recordCallbackUrl=None,
            recordFileFormat=None):
        super(Conference, self).__init__()
        if name is None:
            raise TypeError
        self._value = name
        self.muted = muted
        self.beep = beep
        self.startConferenceOnEnter = startConferenceOnEnter
        self.endConferenceOnExit = endConferenceOnExit
        self.maxParticipants = maxParticipants
        self.waitSound = waitSound
        self.hangupOnStar = hangupOnStar
        self.callbackUrl = callbackUrl
        self.callbackMethod = callbackMethod
        self.digitsMatch = digitsMatch
        self.stayAlone = stayAlone
        self.record = record
        self.recordCallbackUrl = recordCallbackUrl
        self.recordFileFormat = recordFileFormat

        self._content = None

    @property
    def name(self):
        return self._value

    @name.setter
    def name(self, value):
        if value is None:
            raise TypeError
        self._value = value
