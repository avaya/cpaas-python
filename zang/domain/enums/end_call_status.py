# -*- coding: utf-8 -*-

"""
zang.domain.enums.end_call_status
~~~~~~~~~~~~~~~~~~~
Module containing `EndCallStatus` available options
"""
from enum import Enum


class EndCallStatus(Enum):
    CANCELED = 'canceled'
    COMPLETED = 'completed'
