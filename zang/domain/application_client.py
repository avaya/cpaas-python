# -*- coding: utf-8 -*-

"""
zang.domain.application_client
~~~~~~~~~~~~~~~~~~~
`ApplicationClient` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.presence_status import PresenceStatus


class ApplicationClient(BaseResource):

    _strs = [
        'sid',
        'nickname',
        'account_sid',
        'application_sid',
        'client_password',
        'remote_ip',
        'api_version',
        'uri',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _enums = {
        'presence_status': PresenceStatus
    }

    def __init__(self):
        super(ApplicationClient, self).__init__()

    def __repr__(self):
        return '<ApplicationClient at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def nickname(self):
        """Nickname of the client."""
        return self._nickname

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account the application is
        registered with."""
        return self._account_sid

    @property
    def applicationSid(self):
        """An alphanumeric string identifying the application the client is
        registered with."""
        return self._application_sid

    @property
    def clientPassword(self):
        """A one-time password."""
        return self._client_password

    @property
    def remoteIp(self):
        """The IP address of the connecting machine."""
        return self._remote_ip

    @property
    def apiVersion(self):
        """The API version used with this application."""
        return self._api_version

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
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
    def presenceStatus(self):
        """The current status of the client. Possible Values: init, idle,
        loggedin, loggedout"""
        return self._presence_status
