# -*- coding: utf-8 -*-

"""
zang.domain.fraud_control_rule
~~~~~~~~~~~~~~~~~~~
`CnamLookup` model
"""

from zang.domain.base_resource import BaseResource


class FraudControlRule(BaseResource):

    _strs = [
        'country_code',
        'country_name',
        'country_prefix',
        'sid',
    ]
    _reals = [
        'max_outbound_rate',
    ]
    _bools = [
        'is_lock',
        'landline_enabled',
        'mobile_enabled',
        'sms_enabled',
    ]
    _dates = [
        'date_created',
        'date_updated',
        'expiration_date',
    ]

    def __init__(self):
        super(FraudControlRule, self).__init__()

    def __repr__(self):
        return '<FraudControlRule at 0x%x>' % (id(self))

    @property
    def countryCode(self):
        """Two letter country code being whitelisted, authorized or blocked.
        :rtype: str
        """
        return self._country_code

    @property
    def countryName(self):
        """Full name of the destination being whitelisted, authorized or
            blocked.
        :rtype: str
        """
        return self._country_name

    @property
    def countryPrefix(self):
        """Prefix of the destination being whitelisted, authorized or blocked.
        :rtype: str
        """
        return self._country_prefix

    @property
    def dateCreated(self):
        """The date the fraud control resource was created.
        :rtype: date
        """
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the fraud control resource was last updated.
        :rtype: date
        """
        return self._date_updated

    @property
    def expirationDate(self):
        """The date the fraud control resource will expire.
        :rtype: date
        """
        return self._expiration_date

    @property
    def isLock(self):
        """Specifies whether the destinations permission state (blocked,
            whitelisted, etc.) has been locked by our system. Currently,
            the US is locked as a whitelisted destination.
        :rtype: bool
        """
        return self._is_lock

    @property
    def landlineEnabled(self):
        """Landline status for the destination. If false, all landline call
            activity will be rejected or disabled.
        :rtype: bool
        """
        return self._landline_enabled

    @property
    def maxOutboundRate(self):
        """The price limit an outbound call may be. Calls which cost more
            will be rejected.
        :rtype: float
        """
        return self._max_outbound_rate

    @property
    def mobileEnabled(self):
        """Mobile status for the destination. If false, all mobile call
            activity will be rejected or disabled.
        :rtype: bool
        """
        return self._mobile_enabled

    @property
    def sid(self):
        """An alphanumeric string identifying this resource.
        :rtype: str
        """
        return self._sid

    @property
    def smsEnabled(self):
        """Status of the SMS for destination. Can be true or false. If false,
            SMS for same destination will be rejected.
        :rtype: bool
        """
        return self._sms_enabled
