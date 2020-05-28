# -*- coding: utf-8 -*-

"""
zang.domain.account
~~~~~~~~~~~~~~~~~~~
`Account` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.subresource_uris import SubresourceUris


class Account(BaseResource):

    _strs = [
        'friendly_name',
        'sid',
        'status',
        'time_zone',
        'type',
        'uri',
    ]
    _reals = [
        'account_balance',
        'max_outbound_limit',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _map = {
        'subresource_uris': SubresourceUris,
    }

    def __init__(self):
        super(Account, self).__init__()

    def __repr__(self):
        return '<Account at 0x%x>' % (id(self))

    @property
    def accountBalance(self):
        """The current balance of an account."""
        return self._account_balance

    @property
    def dateCreated(self):
        """Date of account creation. Dates are returned in UTC format."""
        return self._date_created

    @property
    def dateUpdated(self):
        """Date of most recent account update. Dates are returned in UTC
        format."""
        return self._date_updated

    @property
    def friendlyName(self):
        """By default, the email used to create the account but a custom alias
        can be set by POSTing a FriendlyName parameter to the
        /Account/{AccountSid} endpoint."""
        return self._friendly_name

    @property
    def maxOutboundLimit(self):
        """The maximum allowed rate per segment. For example, if the
        max_outbound_limit was $1.00 then any calls costing more than $1.00
        per minute would be restricted."""
        return self._max_outbound_limit

    @property
    def sid(self):
        """An alphanumeric string identifying the account."""
        return self._sid

    @property
    def status(self):
        """This is the status of the TelAPI account being requested. The state
        of the status can be either active, suspended, or closed."""
        return self._status

    @property
    def subresourceUris(self):
        """List of an account's various subresources and their URI path.
        Examples of subresources are things like calls that occurred through
        the account, sms messages, purchased phone numbers, etc."""
        return self._subresource_uris

    @property
    def timeZone(self):
        """The name of an accounts timezone."""
        return self._time_zone

    @property
    def type_(self):
        """The type of account being requested. If the account is not yet
        funded Type is "trial". Otherwise, Type for upgraded accounts is
        "full"."""
        return self._type

    @property
    def uri(self):
        """The path appended to the base TelAPI URL, https://api.telapi.com,
        where the resource is located."""
        return self._uri
