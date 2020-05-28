# -*- coding: utf-8 -*-

"""
zang.domain.list.incoming_phone_numbers
~~~~~~~~~~~~~~~~~~~
`Incoming Phone Numbers` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.incoming_phone_number import IncomingPhoneNumber


class IncomingPhoneNumbers(BaseList):

    _arrays = {'incoming_phone_numbers': IncomingPhoneNumber}

    def __init__(self):
        super(IncomingPhoneNumbers, self).__init__()

    @property
    def elements(self):
        return self._incoming_phone_numbers
