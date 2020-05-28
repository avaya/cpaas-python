# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.play_last_recording
~~~~~~~~~~~~~~~~~~~
Module containing `PlayLastRecording` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class PlayLastRecording(BaseNode):

    _allowedContentClass = ()

    def __init__(self):
        self._value = None
        self._content = None
