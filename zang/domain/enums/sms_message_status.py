# -*- coding: utf-8 -*-

"""
zang.domain.enums.sms_message_status
~~~~~~~~~~~~~~~~~~~
Module containing `SmsMessageStatus` available options
"""
from enum import Enum


class SmsMessageStatus(Enum):
    SENT = 'sent'
    SENDING = 'sending'
    QUEUED = 'queued'
    FAILED = 'failed'
