# -*- coding: utf-8 -*-

"""
zang.domain.list.incoming_phone_number
~~~~~~~~~~~~~~~~~~~
`Incoming Phone Number` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.phone_number_type import PhoneNumberType


class IncomingPhoneNumber(BaseResource):

    _strs = [
        'sid',
        'friendly_name',
        'account_sid',
        'voice_url',
        'voice_fallback_url',
        'sms_url',
        'sms_fallback_url',
        'heartbeat_url',
        'status_callback',
        'hangup_callback',
        'api_version',
        'uri',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _bools = [
        'capabilities',
        'voice_caller_id_lookup',
    ]
    _enums = {
        'voice_method': HttpMethod,
        'voice_fallback_method': HttpMethod,
        'sms_method': HttpMethod,
        'sms_fallback_method': HttpMethod,
        'heartbeat_method': HttpMethod,
        'status_callback_method': HttpMethod,
        'hangup_callback_method': HttpMethod,
        'type': PhoneNumberType,
    }

    def __init__(self):
        super(IncomingPhoneNumber, self).__init__()

    def __repr__(self):
        return '<IncomingPhoneNumber at 0x%x>' % (id(self))

    @property
    def sid(self):
        """The HTTP method used when requesting the VoiceStatusCallback."""
        return self._sid

    @property
    def friendlyName(self):
        """User generated name for the incoming number."""
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this phone number is
        registered with."""
        return self._account_sid

    @property
    def type_(self):
        """The type of TelAPI number (local, international, etc.)."""
        return self._type

    @property
    def voiceUrl(self):
        """The URL returning InboundXML incoming calls should execute when
        connected."""
        return self._voice_url

    @property
    def voiceFallbackUrl(self):
        """URL used if any errors occur during execution of InboundXML on a
        call or at initial request of the VoiceUrl."""
        return self._voice_fallback_url

    @property
    def smsUrl(self):
        """The URL returning InboundXML incoming phone numbers should execute
        when receiving an sms."""
        return self._sms_url

    @property
    def smsFallbackUrl(self):
        """URL used if any errors occur during execution of InboundXML from an
        sms or at initial request of the SmsUrl."""
        return self._sms_fallback_url

    @property
    def heartbeatUrl(self):
        """URL that can be used to monitor the phone number."""
        return self._heartbeat_url

    @property
    def statusCallback(self):
        """URL that can be requested to receive notification when and how
        incoming call has ended."""
        return self._status_callback

    @property
    def hangupCallback(self):
        """This is a StatusCallback clone that will be phased out in future
        versions."""
        return self._hangup_callback

    @property
    def apiVersion(self):
        """The API version used with this incoming number."""
        return self._api_version

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
        return self._uri

    @property
    def dateCreated(self):
        """The date the incoming phone number resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the incoming phone number resource was last updated."""
        return self._date_updated

    @property
    def capabilities(self):
        """The features available with this incoming phone number. The
        Elements voice and sms are nested within this property with their
        values as either True or False depending on what the number is capable
        of."""
        return self._capabilities

    @property
    def voiceCallerIdLookup(self):
        """Specifies if the incoming number has voice caller ID lookup
        enabled."""
        return self._voice_caller_id_lookup

    @property
    def voiceMethod(self):
        """Specifies the HTTP method (GET or POST) used to request the
        VoiceUrl once incoming call connects."""
        return self._voice_method

    @property
    def voiceFallbackMethod(self):
        """Specifies the HTTP method (GET or POST) used to request the
        VoiceFallBackUrl if it is needed."""
        return self._voice_fallback_method

    @property
    def smsMethod(self):
        """The HTTP method used when making requests to the SmsUrl. Either GET
        or POST."""
        return self._sms_method

    @property
    def smsFallbackMethod(self):
        """Specifies the HTTP method (GET or POST) used to request the
        SmsFallbackUrl."""
        return self._sms_fallback_method

    @property
    def heartbeatMethod(self):
        """The HTTP method TelAPI will use when requesting the HeartbeatURL.
        Either GET or POST."""
        return self._heartbeat_method

    @property
    def statusCallbackMethod(self):
        """Specifies the HTTP method (GET or POST) used to request the
        HangupCallback URL."""
        return self._status_callback_method

    @property
    def hangupCallbackMethod(self):
        """This is a StatusCallbackMethod clone that will be phased out in
        future versions."""
        return self._hangup_callback_method
