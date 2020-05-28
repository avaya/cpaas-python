# -*- coding: utf-8 -*-

"""
zang.domain.mms_message.py
~~~~~~~~~~~~~~~~~~~
`MmsMessage` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.enums.mms_message_status import MmsMessageStatus
from zang.domain.enums.mms_direction import MmsDirection


class MmsMessage(BaseResource):

    _strs = [
        'apiVersion',
        'mms_sid',
        'account_sid',
        'to',
        'from',
        'body',
        'media_url',
    ]
    _reals = [
    ]
    _dates = [
        'date_created',
    ]
    _enums = {
        'status': MmsMessageStatus,
        'direction': MmsDirection,
    }

    def __init__(self):
        super(MmsMessage, self).__init__()

    def __repr__(self):
        return '<Mms at 0x%x>' % (id(self))

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
    def mediaUrl(self):
        """The Uniform Resource Identifier to this resource."""
        return self._media_url
