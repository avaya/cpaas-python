# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.enums.record_direction
~~~~~~~~~~~~~~~~~~~
Module containing `RecordDirection` available options
"""

from enum import Enum


class RecordDirection(Enum):
    IN = 'in'
    OUT = 'out'
    BOTH = 'both'
