# -*- coding: utf-8 -*-

"""
zang.domain.bna_lookup
~~~~~~~~~~~~~~~~~~~
`BnaLookup` model
"""

from zang.domain.base_resource import BaseResource


class BnaLookup(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'phone_number',
        'first_name',
        'last_name',
        'address',
        'city',
        'state',
        'zip_code',
        'country_code',
        'api_version',
        'uri',
    ]
    _reals = [
        'price',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]

    def __init__(self):
        super(BnaLookup, self).__init__()

    def __repr__(self):
        return '<BnaLookup at 0x%x>' % (id(self))

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
    def firstName(self):
        """The first name of the individual associated with this phone number.
        :rtype: str
        """
        return self._first_name

    @property
    def lastName(self):
        """The last name of the individual associated with this phone number.
        :rtype: str
        """
        return self._last_name

    @property
    def address(self):
        """The address associated with this phone number.
        :rtype: str
        """
        return self._address

    @property
    def city(self):
        """The city associated with this phone number.
        :rtype: str
        """
        return self._city

    @property
    def state(self):
        """The US state associated with this phone number.
        :rtype: str
        """
        return self._state

    @property
    def zipCode(self):
        """The zip code associated with this phone number.
        :rtype: str
        """
        return self._zip_code

    @property
    def countryCode(self):
        """The country code associated with this phone number.
            (BNA lookups are currently only available in US)
        :rtype: str
        """
        return self._country_code

    @property
    def price(self):
        """The price to perform the lookup. If only the city and state of
            the number are looked up, you are charged $.01. If a full address
            lookup is successful you are charged $.15.
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
