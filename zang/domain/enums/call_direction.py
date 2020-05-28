# -*- coding: utf-8 -*-

"""
zang.domain.enums.call_direction
~~~~~~~~~~~~~~~~~~~
Module containing `CallDirection` available options
"""
from enum import Enum


class CallDirection(Enum):
    INBOUND = 'inbound'
    OUTBOUND_API = 'outbound-api'
    OUTBOUND_DIAL = 'outbound-dial'
    UNKNOWN = 'unknown'
