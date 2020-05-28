# -*- coding: utf-8 -*-

"""
zang.domain.enums.mms_direction
~~~~~~~~~~~~~~~~~~~
Module containing `MmsDirection` available options
"""
from enum import Enum


class MmsDirection(Enum):
    OUTBOUND_API = 'outbound-api'
    INCOMING = 'incoming'
    OUTBOUND_CALL = 'outbound-call'
    OUTBOUND_REPLY = 'outbound-reply'
    OUTBOUND = 'outbound'
