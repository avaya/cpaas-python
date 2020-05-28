# -*- coding: utf-8 -*-

"""
zang.domain.transcription
~~~~~~~~~~~~~~~~~~~
`Transcription` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.transcribe_quality import TranscribeQuality
from zang.domain.enums.transcription_status import TranscriptionStatus


class Transcription(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'audio_url',
        'recording_sid',
        'transcription_text',
        'api_version',
        'transcribe_callback',
        'uri',
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
    _enums = {
        'type': TranscribeQuality,
        'status': TranscriptionStatus,
        'callback_method': HttpMethod,
    }

    def __init__(self):
        super(Transcription, self).__init__()

    def __repr__(self):
        return '<Transcription at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this transcription
        occurred through."""
        return self._account_sid

    @property
    def dateCreated(self):
        """The date the transcription resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the transcription resource was last updated."""
        return self._date_updated

    @property
    def status(self):
        """Status of the transcription. May be in-progress, completed,
        or failed."""
        return self._status

    @property
    def type_(self):
        """Transcription quality tier. May be auto or hybrid. Default is
        auto."""
        return self._type_

    @property
    def audioUrl(self):
        """URL where a file containing the transcribed audio is located."""
        return self._audio_url

    @property
    def recordingSid(self):
        """An alphanumeric string used to identify the recording that was
        transcribed. This field is only returned for transcriptions of TelAPI
        recordings."""
        return self._recording_sid

    @property
    def duration(self):
        """Length in seconds of the transcribed recording."""
        return self._duration

    @property
    def transcriptionText(self):
        """Text of the transcribed audio."""
        return self._transcription_text

    @property
    def apiVersion(self):
        """The API version being used when the transcription was made."""
        return self._api_version

    @property
    def price(self):
        """Cost of the transcription."""
        return self._price

    @property
    def transcribeCallback(self):
        """URL where transcription will report to after completion."""
        return self._transcribe_callback

    @property
    def callbackMethod(self):
        """Method to request TranscribeCallback URL. May be POST or GET.
        Default is POST."""
        return self._callback_method

    @property
    def uri(self):
        """The URL to this resource."""
        return self._uri
