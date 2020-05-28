# -*- coding: utf-8 -*-

"""
zang.domain.enums.sms_direction
~~~~~~~~~~~~~~~~~~~
Module containing `SmsDirection` available options
"""
from enum import Enum


class SmsDirection(Enum):
    OUTBOUND_API = 'outbound-api'
    INCOMING = 'incoming'
    OUTBOUND_CALL = 'outbound-call'
    OUTBOUND_REPLY = 'outbound-reply'
