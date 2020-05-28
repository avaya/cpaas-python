# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.enums.reject_reason
~~~~~~~~~~~~~~~~~~~
Module containing `RejectReason` available options
"""

from enum import Enum


class RejectReason(Enum):
    BUSY = 'busy'
    REJECTED = 'rejected'
