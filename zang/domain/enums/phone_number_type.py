# -*- coding: utf-8 -*-

"""
zang.domain.enums.log_level
~~~~~~~~~~~~~~~~~~~
Module containing `PhoneNumberType` available options
"""
from enum import Enum


class PhoneNumberType(Enum):
    LOCAL = 'local'
    INTERNATIONAL = 'international'
    TOLL_FREE = 'toll-free'
