# -*- coding: utf-8 -*-

"""
zang.domain.enums.mms_message_status
~~~~~~~~~~~~~~~~~~~
Module containing `MmsMessageStatus` available options
"""
from enum import Enum


class MmsMessageStatus(Enum):
    SENT = 'sent'
    SENDING = 'sending'
    QUEUED = 'queued'
    FAILED = 'failed'
