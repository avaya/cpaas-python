# -*- coding: utf-8 -*-

"""
zang.domain.domain
~~~~~~~~~~~~~~~~~~~
`Domain` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.auth_type import AuthType


class Domain(BaseResource):

    _strs = [
        'sid',
        'friendly_name',
        'account_sid',
        'domain_name',
        'voice_url',
        'voice_fallback_url',
        'voice_heartbeat_callback',
        'voice_status_callback_url',
        'uri',
        'domain_sip_url',
        'subresource_uris',
        'ip_access_control_list_mappings',
        'credential_list_mappings',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _enums = {
        'auth_type': AuthType,
        'voice_method': HttpMethod,
        'voice_fallback_method': HttpMethod,
        'voice_heartbeat_callback_method': HttpMethod,
        'voice_status_callback_method': HttpMethod,
    }

    def __init__(self):
        super(Domain, self).__init__()

    def __repr__(self):
        return '<Domain at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def friendlyName(self):
        """A human-readable name associated with this domain."""
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with this
        resource."""
        return self._account_sid

    @property
    def domainName(self):
        """A unique address through which you route your SIP traffic to
        TelAPI."""
        return self._domain_name

    @property
    def authType(self):
        """The types of authentication associated with your domain. You must
        have at least one or all requests will be blocked. Allowed Values:
        IP_ACL and/or CREDENTIAL_LIST"""
        return self._auth_type

    @property
    def voiceUrl(self):
        """The URL requested when a call is received by your domain."""
        return self._voice_url

    @property
    def voiceFallbackUrl(self):
        """The URL requested if the VoiceUrl fails."""
        return self._voice_fallback_url

    @property
    def voiceHeartbeatCallback(self):
        """URL that can be requested every 60 seconds during the call to
        notify of elapsed time and pass other general information."""
        return self._voice_heartbeat_callback

    @property
    def voiceStatusCallbackUrl(self):
        """The URL that TelAPI will use to send you status notifications
        regarding your SIP call."""
        return self._voice_status_callback_url

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
        return self._uri

    @property
    def domainSipUrl(self):
        """Complete URL for this SIP domain."""
        return self._domain_sip_url

    @property
    def subresourceUris(self):
        """URIs for managing this resource (IP access control and
        credentials)."""
        return self._subresource_uris

    @property
    def ipAccessControlListMappings(self):
        """URI for IP access controll management."""
        return self._ip_access_control_list_mappings

    @property
    def credentialListMappings(self):
        """URI for credentials management."""
        return self._credential_list_mappings

    @property
    def dateCreated(self):
        """The date this credential was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the application resource was last updated."""
        return self._date_updated

    @property
    def voiceMethod(self):
        """The HTTP method used when requesting the VoiceUrl."""
        return self._voice_method

    @property
    def voiceFallbackMethod(self):
        """The HTTP method used when requesting the VoiceFallbackUrl."""
        return self._voice_fallback_method

    @property
    def voiceHeartbeatCallbackMethod(self):
        """Specifies the HTTP method used to request HeartbeatUrl.
            Default Value: POST. Allowed Value: POST or GET"""
        return self._voice_heartbeat_callback_method

    @property
    def voiceStatusCallbackMethod(self):
        """The HTTP method used when requesting the VoiceStatusCallback."""
        return self._voice_status_callback_method
