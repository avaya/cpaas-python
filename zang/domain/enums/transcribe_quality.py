# -*- coding: utf-8 -*-

"""
zang.domain.enums.transcribe_quality
~~~~~~~~~~~~~~~~~~~
Module containing `TranscribeQuality` available options
"""
from enum import Enum


class TranscribeQuality(Enum):
    AUTO = 'auto'
    HYBRID = 'hybrid'
    KEYWORDS = 'keywords'
