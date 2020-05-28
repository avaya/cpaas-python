# -*- coding: utf-8 -*-

"""
zang.domain.enums.call_status
~~~~~~~~~~~~~~~~~~~
Module containing `CallStatus` available options
"""
from enum import Enum


class CallStatus(Enum):
    BUSY = 'busy'
    CANCELED = 'canceled'
    COMPLETED = 'completed'
    FAILED = 'failed'
    IN_PROGRESS = 'in-progress'
    NO_ANSWER = 'no-answer'
    PRE_QUEUED = 'pre-queued'
    QUEUED = 'queued'
    RINGING = 'ringing'
    UNKNOWN = 'unknown'
