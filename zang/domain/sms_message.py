# -*- coding: utf-8 -*-

"""
zang.domain.sms_message.py
~~~~~~~~~~~~~~~~~~~
`SmsMessage` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.enums.sms_message_status import SmsMessageStatus
from zang.domain.enums.sms_direction import SmsDirection


class SmsMessage(BaseResource):

    _strs = [
        'api_version',
        'sid',
        'account_sid',
        'to',
        'from',
        'body',
        'uri',
    ]
    _reals = [
        'price',
    ]
    _dates = [
        'date_created',
        'date_updated',
        'date_sent',
    ]
    _enums = {
        'status': SmsMessageStatus,
        'direction': SmsDirection,
    }

    def __init__(self):
        super(SmsMessage, self).__init__()

    def __repr__(self):
        return '<Sms at 0x%x>' % (id(self))

    @property
    def apiVersion(self):
        """The Api Version being used."""
        return self._api_version

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this call occurred
        through."""
        return self._account_sid

    @property
    def dateCreated(self):
        """The date the SMS resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the SMS resource was last updated."""
        return self._date_updated

    @property
    def dateSent(self):
        """The date the SMS was sent."""
        return self._date_sent

    @property
    def to(self):
        """The number that received the SMS message."""
        return self._to

    @property
    def from_(self):
        """The number that sent the SMS message."""
        return self._from

    @property
    def body(self):
        """Text of the SMS message sent or received. May be up to 160
        characters in length."""
        return self._body

    @property
    def status(self):
        """Status of the SMS: sent, sending, queued, or failed."""
        return self._status

    @property
    def direction(self):
        """Specifies the direction of the SMS: messages from REST API are
        “outbound-api”, messages from incoming phone numbers to TelAPI are
        “incoming”, messages from InboundXML initiated during an outbound
        call are “outbound-call”, and messages from InboundXML initiated via
        an sms reply are “outbound-reply”."""
        return self._direction

    @property
    def price(self):
        """Cost of the SMS."""
        return self._price

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
        return self._uri
