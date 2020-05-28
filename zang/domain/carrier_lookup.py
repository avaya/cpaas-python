# -*- coding: utf-8 -*-

"""
zang.domain.carrier_lookup
~~~~~~~~~~~~~~~~~~~
`Carrier` model
"""

from zang.domain.base_resource import BaseResource


class CarrierLookup(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'phone_number',
        'network',
        'country_code',
        'mnc',
        'mcc',
        'api_version',
        'uri',
    ]
    _ints = [
        'carrier_id',
    ]
    _reals = [
        'price',
    ]
    _bools = [
        'mobile',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]

    def __init__(self):
        super(CarrierLookup, self).__init__()

    def __repr__(self):
        return '<CarrierLookup at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource.
        :rtype: str
        """
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account this lookup occurred through.
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
    def network(self):
        """The carrier the phone number is currently operating on.
        :rtype: str
        """
        return self._network

    @property
    def mobile(self):
        """Boolean value specifying whether the phone number is mobile.
        :rtype: bool
        """
        return self._mobile

    @property
    def carrierId(self):
        """Four digit Carrier Identification Code.
        :rtype: int
        """
        return self._carrier_id

    @property
    def countryCode(self):
        """The iso country code of the mobile number.
        :rtype: str
        """
        return self._country_code

    @property
    def mnc(self):
        """The Mobile Network Code is only returned if available. It is used
        in conjunction with Mcc to uniquely identify a carrier.
        :rtype: str
        """
        return self._mnc

    @property
    def mcc(self):
        """The Mobile Country Code is only returned if available. It is used
        in conjunction with Mnc to uniquely identify a carrier.
        :rtype: str
        """
        return self._mcc

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
