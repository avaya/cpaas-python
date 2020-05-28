# -*- coding: utf-8 -*-

"""
zang.domain.call
~~~~~~~~~~~~~~~~~~~
`Call` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.answered_by import AnsweredBy
from zang.domain.enums.call_status import CallStatus
from zang.domain.enums.call_direction import CallDirection


class Call(BaseResource):

    _strs = [
        'sid',
        'parent_call_sid',
        'account_sid',
        'to',
        'from',
        'phone_number_sid',
        'api_version',
        'forwarded_from',
        'uri',
        'subresource_uris',
    ]
    _ints = [
        'duration',
        'recordings_count',
    ]
    _reals = [
        'price',
    ]
    _bools = [
        'caller_id_blocked',
    ]
    _dates = [
        'date_created',
        'date_updated',
        'start_time',
        'end_time',
    ]
    _enums = {
        'answered_by': AnsweredBy,
        'status': CallStatus,
        'direction': CallDirection,
    }

    def __init__(self):
        super(Call, self).__init__()

    def __repr__(self):
        return '<Call at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def parentCallSid(self):
        """If the call was created during a different call using InboundXML,
        this is the sid of that initiating call."""
        return self._parent_call_sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this call occurred
        through."""
        return self._account_sid

    @property
    def to(self):
        """The number that was called."""
        return self._to

    @property
    def from_(self):
        """The number that initiated the call."""
        return self._from

    @property
    def phoneNumberSid(self):
        """The sid of the TelAPI number calling, or being called. If no TelAPI
        phone number is involved in the call, this property is empty."""
        return self._phone_number_sid

    @property
    def direction(self):
        """The direction of the call from the perspective of TelAPI. "inbound"
        for calls to TelAPI, "outbound-api" for calls from the TelAPI via REST
        request, or "outbound-dial" for calls from TelAPI via InboundXML."""
        return self._direction

    @property
    def answeredBy(self):
        """If the initiated call has answering machine detection, this
        specifies whether the machine answered. Can be "human", "machine" or
        "tbd" (to be determined)."""
        return self._answered_by

    @property
    def apiVersion(self):
        """The Api Version being used."""
        return self._api_version

    @property
    def forwardedFrom(self):
        """The number that forwarded the call, if any."""
        return self._forwarded_from

    @property
    def callerIdBlocked(self):
        """Specifies whether the caller ID of the inbound phone number was
        blocked."""
        return self._caller_id_blocked

    @property
    def uri(self):
        """The URL pointing to this resource."""
        return self._uri

    @property
    def subresourceUris(self):
        """List of a call's various subresources and their URL paths. Examples
        of call subresources are notifications, recordings, etc."""
        return self._subresource_uris

    @property
    def duration(self):
        """The length of the call in seconds."""
        return self._duration

    @property
    def recordingsCount(self):
        """The number of recordings made during this call."""
        return self._recordings_count

    @property
    def price(self):
        """The cost of the call, if available."""
        return self._price

    @property
    def dateCreated(self):
        """The date the call resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the call resource was last updated."""
        return self._date_updated

    @property
    def startTime(self):
        """The date and time the call started."""
        return self._start_time

    @property
    def endTime(self):
        """The date and time the call ended."""
        return self._end_time

    @property
    def callStatus(self):
        """The status of the call: queued, ringing, in-progress, completed,
        failed, busy, no-answer."""
        return self._status
