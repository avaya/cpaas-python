# -*- coding: utf-8 -*-

"""
zang.domain.list.recording
~~~~~~~~~~~~~~~~~~~
`Recording` model
"""

from zang.domain.base_resource import BaseResource


class Recording(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'call_sid',
        'recording_url',
        'api_version',
        'uri'
    ]
    _ints = [
        'duration',
    ]
    _reals = [
        'price',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]

    def __init__(self):
        super(Recording, self).__init__()

    def __repr__(self):
        return '<Recording at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with this
        recording."""
        return self._account_sid

    @property
    def callSid(self):
        """The sid identifying the recorded call."""
        return self._call_sid

    @property
    def recordingUrl(self):
        """The URL where the mp3 file of the recording is located."""
        return self._recording_url

    @property
    def apiVersion(self):
        """The API version being used when the recording was made."""
        return self._api_version

    @property
    def duration(self):
        """Time of recording in seconds."""
        return self._duration

    @property
    def price(self):
        """The cost of this recording."""
        return self._price

    @property
    def dateCreated(self):
        """The date the recording resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the recording resource was last updated."""
        return self._date_updated

    @property
    def uri(self):
        """The URL to this resource."""
        return self._uri
