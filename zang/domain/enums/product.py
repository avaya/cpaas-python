# -*- coding: utf-8 -*-

"""
zang.domain.enums.product
~~~~~~~~~~~~~~~~~~~
Module containing `Product` available options
"""
from enum import Enum


class Product(Enum):
    OUTBOUND_CALL = 'Outbound Call'
    INBOUND_CALL = 'Inbound Call'
    OUTBOUND_SMS = 'Outbound SMS'
    INBOUND_SMS = 'Inbound SMS'
    OUTBOUND_SIP = 'Outbound SIP'
    INBOUND_SIP = 'Inbound SIP'
    RECORDING = 'Recording'
    RECURRING_DID = 'Recurring DID'
    RECURRING_DID_PREMIUM = 'Recurring DID (Premium)'
    TRANSCRIPTION_AUTO = 'Transcription (Auto)'
    TRANSCRIPTION_HYBRID = 'Transcription (Hybrid)'
    RECURRING_INBOUND_CHANNEL = 'Recurring Inbound Channel'
    INBOUND_CALL_CHANNEL = 'Inbound Call (Channel)'
    CNAM_DIP = 'CNAM Dip'
    CARRIER_LOOKUP = 'Carrier Lookup'
    OUTBOUND_CALL_SPOOFED = 'Outbound Call (Spoofed)'
    INBOUND_CALL_CHANNEL_OVERAGE = 'Inbound Call (Channel Overage)'
    RECURRING_DID_UNBLOCK = 'Recurring DID Unblock'
    INBOUND_CALL_UNBLOCKED = 'Inbound Call Unblocked'
    INBOUND_CALL_FORWARDED_FROM = 'Inbound Call Forwarded From'

    @classmethod
    def ordinal(cls, key):
        map_ = {
            cls.OUTBOUND_CALL: 1,
            cls.INBOUND_CALL: 2,
            cls.OUTBOUND_SMS: 3,
            cls.INBOUND_SMS: 4,
            cls.OUTBOUND_SIP: 5,
            cls.INBOUND_SIP: 6,
            cls.RECORDING: 7,
            cls.RECURRING_DID: 8,
            cls.RECURRING_DID_PREMIUM: 9,
            cls.TRANSCRIPTION_AUTO: 12,
            cls.TRANSCRIPTION_HYBRID: 14,
            cls.RECURRING_INBOUND_CHANNEL: 17,
            cls.INBOUND_CALL_CHANNEL: 18,
            cls.CNAM_DIP: 19,
            cls.CARRIER_LOOKUP: 20,
            cls.OUTBOUND_CALL_SPOOFED: 21,
            cls.INBOUND_CALL_CHANNEL_OVERAGE: 22,
            cls.RECURRING_DID_UNBLOCK: 23,
            cls.INBOUND_CALL_UNBLOCKED: 24,
            cls.INBOUND_CALL_FORWARDED_FROM: 25,
        }
        return map_[key]
