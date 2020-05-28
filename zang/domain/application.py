from zang.domain.base_resource import BaseResource
from zang.domain.enums.http_method import HttpMethod


class Application(BaseResource):

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
    }

    def __init__(self):
        super(Application, self).__init__()

    def __repr__(self):
        return '<Application at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def friendlyName(self):
        """User generated name of the application."""
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account the application is
        registered with."""
        return self._account_sid

    @property
    def voiceUrl(self):
        """The URL requested once the call connects, returning InboundXML with
        instructions on how to process your call."""
        return self._voice_url

    @property
    def voiceFallbackUrl(self):
        """URL used if the required URL is unavailable or if any errors occur
        during execution of the InboundXML returned by the required URL"""
        return self._voice_fallback_url

    @property
    def smsUrl(self):
        """The URL requested when an SMS is received, returning InboundXML
        with instructions on how to process your SMS."""
        return self._sms_url

    @property
    def smsFallbackUrl(self):
        """URL used if the required URL is unavailable or if any errors occur
        during execution of the InboundXML returned by the required URL."""
        return self._sms_fallback_url

    @property
    def heartbeatUrl(self):
        """A URL that will be requested every 60 seconds during the call,
        sending information about the call."""
        return self._heartbeat_url

    @property
    def statusCallback(self):
        """A URL that will be requested when the call connects and ends,
        sending information about the call."""
        return self._status_callback

    @property
    def hangupCallback(self):
        """This is a StatusCallback clone that will be phased out in future
        versions."""
        return self._hangup_callback

    @property
    def apiVersion(self):
        """The API version used with this application."""
        return self._api_version

    @property
    def uri(self):
        """The URL to this resource."""
        return self._uri

    @property
    def dateCreated(self):
        """The date the application resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the application resource was last updated."""
        return self._date_updated

    @property
    def voiceCallerIdLookup(self):
        """Specifies if the application has voice caller ID lookup enabled."""
        return self._voice_caller_id_lookup

    @property
    def voiceMethod(self):
        """The HTTP method used to request the URL once the call connects."""
        return self._voice_method

    @property
    def voiceFallbackMethod(self):
        """The HTTP method used to request the FallbackUrl once the call
        connects."""
        return self._voice_fallback_method

    @property
    def smsMethod(self):
        """The HTTP method used to request the URL when an SMS is received."""
        return self._sms_method

    @property
    def smsFallbackMethod(self):
        """The HTTP method used to request the FallbackUrl once the call
        connects."""
        return self._sms_fallback_method

    @property
    def heartbeatMethod(self):
        """The HTTP method used to request the HeartbeatUrl."""
        return self._heartbeat_method

    @property
    def statusCallbackMethod(self):
        """The HTTP method used to request the StatusCallback URL."""
        return self._status_callback_method

    @property
    def hangupCallbackMethod(self):
        """This is a StatusCallbackMethod clone that will be phased out in
        future versions."""
        return self._hangup_callback_meth
