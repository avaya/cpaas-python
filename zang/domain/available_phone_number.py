# -*- coding: utf-8 -*-

"""
zang.domain.available_phone_number
~~~~~~~~~~~~~~~~~~~
`AvailablePhoneNumber` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.enums.available_number_type import AvailableNumberType


class AvailablePhoneNumber(BaseResource):

    _bools = [
        'sms_enabled',
        'supports_forwarded_from',
        'voice_enabled',
    ]

    _reals = [
        'monthly_cost',
        'per_minute_cost',
        'setup_cost',
    ]

    _strs = [
        'city',
        'country_code',
        'exchange',
        'friendly_name',
        'iso_country',
        'lata',
        'latitude',
        'longitude',
        'npa',
        'phone_number',
        'postal_code',
        'rate_center',
        'region',
    ]
    _enums = {
        'type': AvailableNumberType,
    }

    def __init__(self):
        super(AvailablePhoneNumber, self).__init__()

    def friendlyName(self):
        """Domestic format version of the available phone number.
        (e.g. 1234567890 to (123)-456-7890).
        :rtype: str
        """
        return self._friendly_name

    @property
    def phoneNumber(self):
        """The E.164 format number of each available number.
        :rtype: str
        """
        return self._phone_number

    @property
    def lata(self):
        """Local Access and Transportation Area of the available number.
        The LATA is determined by geographical region.
        :rtype: str
        """
        return self._lata

    @property
    def rateCenter(self):
        """The available phone numbers rate center.
        :rtype: str
        """
        return self._rate_center

    @property
    def latitude(self):
        """The latitude of the available phone number.
        :rtype: str
        """
        return self._latitude

    @property
    def longitude(self):
        """The longitude of the available phone number.
        :rtype: str
        """
        return self._longitude

    @property
    def countryCode(self):
        """Code used to identify the phone numbers geographic origin.
        Found at the beginning of the number.
        :rtype: str
        """
        return self._country_code

    @property
    def npa(self):
        """Numbering Plan Area of the available number.
        This is more commonly known as the area code.
        :rtype: str
        """
        return self._npa

    @property
    def exchange(self):
        """Three digits following the NPA (area code) in the available
        number.
        :rtype: str
        """
        return self._exchange

    @property
    def city(self):
        """The available phone numbers city.
        :rtype: str
        """
        return self._city

    @property
    def region(self):
        """The region of the available phone number.
        Usually a two letter abbreviation.
        :rtype: str
        """
        return self._region

    @property
    def postalCode(self):
        """The postal code (also known as zip code) of the available number.
        :rtype: str
        """
        return self._postal_code

    @property
    def isoCountry(self):
        """Two letter country code of the available phone number.
        :rtype: str
        """
        return self._iso_country

    @property
    def type_(self):
        """Type of phone number (local or tollfree).
        :rtype: zang.domain.enums.available_number_type.AvailableNumberType
        """
        return self._type

    @property
    def setupCost(self):
        """Cost of phone number setup.
        :rtype: float
        """
        return self._setup_cost

    @property
    def monthlyCost(self):
        """Cost of phone number per month.
        :rtype: float
        """
        return self._monthly_cost

    @property
    def perMinuteCost(self):
        """Cost of phone number per month.
        :rtype: float
        """
        return self._per_minute_cost

    @property
    def voiceEnabled(self):
        """Is voice enabled for this phone number? Can be true or false.
        :rtype: bool
        """
        return self._voice_enabled

    @property
    def smsEnabled(self):
        """Is SMS enabled for this phone number? Can be true or false.
        :rtype: bool
        """
        return self._sms_enabled

    @property
    def supportsForwardedFrom(self):
        """Does phone number support forwarded from? Can be true or false.
        :rtype: bool
        """
        return self._supports_forwarded_from
