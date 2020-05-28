# -*- coding: utf-8 -*-

"""
zang.domain.enums.transcription_status
~~~~~~~~~~~~~~~~~~~
Module containing `TranscriptionStatus` available options
"""
from enum import Enum


class TranscriptionStatus(Enum):
    COMPLETED = 'completed'
    IN_PROGRESS = 'in-progress'
    FAILED = 'failed'
