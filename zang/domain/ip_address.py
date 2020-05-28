# -*- coding: utf-8 -*-

"""
zang.domain.list.ip_address
~~~~~~~~~~~~~~~~~~~
`IpAddress` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.subresource_uris import SubresourceUris


class IpAddress(BaseResource):

    _strs = [
        'sid',
        'friendly_name',
        'ip_address',
        'account_sid',
        'uri',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _map = {
        'subresource_uris': SubresourceUris,
    }

    def __init__(self):
        super(IpAddress, self).__init__()

    def __repr__(self):
        return '<IpAddress at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource.
        :rtype: str
        """
        return self._sid

    @property
    def friendlyName(self):
        """A human-readable name associated with this domain.
        :rtype: str
        """
        return self._friendly_name

    @property
    def ipAddress(self):
        """An IP address from which you wish to accept traffic.
            At this time, only IPv4 supported.
        :rtype: str
        """
        return self._ip_address

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with
            this resource.
        :rtype: str
        """
        return self._account_sid

    @property
    def dateCreated(self):
        """The date this IP address was created.
        :rtype: date
        """
        return self._date_created

    @property
    def dateUpdated(self):
        """The date this IP address was last updated.
        :rtype: date
        """
        return self._date_updated

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource.
        :rtype: str
        """
        return self._uri

    @property
    def subresourceUris(self):
        """URIs used for managing this resource.
        :rtype: zang.domain.subresource_uris.SubresourceUris
        """
        return self._subresource_uris
