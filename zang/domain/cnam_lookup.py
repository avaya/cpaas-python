# -*- coding: utf-8 -*-

"""
zang.domain.cnam_lookup
~~~~~~~~~~~~~~~~~~~
`CnamLookup` model
"""

from zang.domain.base_resource import BaseResource


class CnamLookup(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'uri',
        'phone_number',
        'body',
        'api_version',
    ]
    _reals = [
        'price',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]

    def __init__(self):
        super(CnamLookup, self).__init__()

    def __repr__(self):
        return '<CnamLookup at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource.
        :rtype: str
        """
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this lookup
        occurred through.
        :rtype: str
        """
        return self._account_sid

    @property
    def dateCreated(self):
        """The date the lookup resource was created.
        :rtype: date
        """
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the lookup resource was last updated.
        :rtype: date
        """
        return self._date_updated

    @property
    def phoneNumber(self):
        """The phone number the lookup was performed on.
        :rtype: str
        """
        return self._phone_number

    @property
    def body(self):
        """The result of our CNAM lookup. Usually a name or organisation
        associated with this phone.
        :rtype: str
        """
        return self._body

    @property
    def price(self):
        """The cost of the lookup.
        :rtype: float
        """
        return self._price

    @property
    def apiVersion(self):
        """The API version being used when the carrier lookup was made.
        :rtype: str
        """
        return self._api_version

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource.
        :rtype: str
        """
        return self._uri
