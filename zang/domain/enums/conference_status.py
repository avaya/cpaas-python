# -*- coding: utf-8 -*-

"""
zang.domain.enums.conference_status
~~~~~~~~~~~~~~~~~~~
Module containing `ConferenceStatus` available options
"""
from enum import Enum


class ConferenceStatus(Enum):
    INIT = 'init'
    IN_PROGRESS = 'in-progress'
    COMPLETED = 'completed'
