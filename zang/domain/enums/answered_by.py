# -*- coding: utf-8 -*-

"""
zang.domain.enums.answered_by
~~~~~~~~~~~~~~~~~~~
Module containing `AnsweredBy` available options
"""
from enum import Enum


class AnsweredBy(Enum):
    HUMAN = 'human'
    MACHINE = 'machine'
    TBD = 'tbd'
    NOBODY = 'nobody'
    UNKNOWN = 'unknown'
