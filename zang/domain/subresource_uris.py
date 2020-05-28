from zang.domain.base_resource import BaseResource


class SubresourceUris (BaseResource):

    _strs = [
        'available_phone_numbers',
        'calls',
        'conferences',
        'incoming_phone_numbers',
        'notifications',
        'recordings',
        'smsMessages',
        'transcriptions',
        'transactions',
        'applications',
        'fraud',
        'cnam',
        'bna',
        'carrier',
        'usages',
    ]

    def __init__(self):
        super(SubresourceUris, self).__init__()

    def __repr__(self):
        return '<SubresourceUris at 0x%x>' % (id(self))

    @property
    def availablePhoneNumbers(self):
        return self._available_phone_numbers

    @property
    def calls(self):
        return self._calls

    @property
    def conferences(self):
        return self._conferences

    @property
    def incomingPhoneNumbers(self):
        return self._incoming_phone_numbers

    @property
    def notifications(self):
        return self._notifications

    @property
    def recordings(self):
        return self._recordings

    @property
    def smsMessages(self):
        return self._smsMessages

    @property
    def transcriptions(self):
        return self._transcriptions

    @property
    def transactions(self):
        return self._transactions

    @property
    def applications(self):
        return self._applications

    @property
    def fraud(self):
        return self._fraud

    @property
    def cnam(self):
        return self._cnam

    @property
    def bna(self):
        return self._bna

    @property
    def carrier(self):
        return self._carrier

    @property
    def usages(self):
        return self._usages
