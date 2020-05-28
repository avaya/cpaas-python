# -*- coding: utf-8 -*-

"""
zang.domain.list.recording
~~~~~~~~~~~~~~~~~~~
`AvailablePhoneNumbers` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.available_phone_number import AvailablePhoneNumber


class AvailablePhoneNumbers(BaseList):

    _arrays = {'available_phone_numbers': AvailablePhoneNumber}

    def __init__(self):
        super(AvailablePhoneNumbers, self).__init__()

    @property
    def elements(self):
        return self._available_phone_numbers
