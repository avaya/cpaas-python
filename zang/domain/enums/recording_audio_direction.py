# -*- coding: utf-8 -*-

"""
zang.domain.enums.recording_audio_direction
~~~~~~~~~~~~~~~~~~~
Module containing `RecordingAudioDirection` available options
"""
from enum import Enum


class RecordingAudioDirection(Enum):
    IN = 'in'
    OUT = 'out'
    BOTH = 'both'
