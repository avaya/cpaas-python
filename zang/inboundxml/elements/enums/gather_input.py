# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.enums.gather_input
~~~~~~~~~~~~~~~~~~~
Module containing `GatherInput` available options
"""

from enum import Enum


class GatherInput(Enum):
    SPEECH = 'speech'
    DTMF = 'dtmf'
    SPEECH_DTMF = 'speech dtmf'
