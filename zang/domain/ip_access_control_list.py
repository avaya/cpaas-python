# -*- coding: utf-8 -*-

"""
zang.domain.list.recording
~~~~~~~~~~~~~~~~~~~
`IpAccessControlList` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.subresource_uris import SubresourceUris


class IpAccessControlList(BaseResource):

    _strs = [
        'sid',
        'friendly_name',
        'account_sid',
        'uri',
        'credentials',
    ]
    _ints = [
        'ip_addresses_count',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _map = {
        'subresource_uris': SubresourceUris,
    }

    @property
    def sid(self):
        """An alphanumeric string identifying this resource.
        :rtype: str
        """
        return self._sid

    @property
    def friendlyName(self):
        """A human-readable name associated with this IP access control list.
        :rtype: str
        """
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with
        this resource.
        :rtype: str
        """
        return self._account_sid

    @property
    def dateCreated(self):
        """The date this credential was created.
        :rtype: date
        """
        return self._date_created

    @property
    def dateUpdated(self):
        """The date this credential was last updated.
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
    def ipAddressesCount(self):
        """Number of the assigned IP addresses on this IP access control list.
        :rtype: int
        """
        return self._ip_addresses_count

    @property
    def subresourceUris(self):
        """URIs used for managing this resource.
        :rtype: zang.domain.subresource_uris.SubresourceUris
        """
        return self._subresource_uris

    @property
    def credentials(self):
        """URI for managing credentials on this IP access control list.
        :rtype: str
        """
        return self._credentials
