# -*- coding: utf-8 -*-

"""
zang.domain.enums.if_machine
~~~~~~~~~~~~~~~~~~~
Module containing `IfMachine` available options
"""
from enum import Enum


class IfMachine(Enum):
    CONTINUE = 'continue'
    REDIRECT = 'redirect'
    HANGUP = 'hangup'
