# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.record
~~~~~~~~~~~~~~~~~~~
Module containing `Record` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Record(BaseNode):

    _allowedContentClass = ()

    def __init__(
            self,
            action=None,
            method=None,
            timeout=None,
            finishOnKey=None,
            maxLength=None,
            transcribe=None,
            transcribeQuality=None,
            transcribeCallback=None,
            playBeep=None,
            direction=None,
            fileFormat=None,
            background=None,
            trimSilence=None):
        self.action = action
        self.method = method
        self.timeout = timeout
        self.finishOnKey = finishOnKey
        self.maxLength = maxLength
        self.transcribe = transcribe
        self.transcribeQuality = transcribeQuality
        self.transcribeCallback = transcribeCallback
        self.playBeep = playBeep
        self.direction = direction
        self.fileFormat = fileFormat
        self.background = background
        self.trimSilence = trimSilence

        self._value = None
        self._content = None
