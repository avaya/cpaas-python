# -*- coding: utf-8 -*-

"""
zang.domain.list.carrier_lookups
~~~~~~~~~~~~~~~~~~~
`CarrierLookups` model
"""
from zang.domain.list.base_list import BaseList
from zang.domain.carrier_lookup import CarrierLookup


class CarrierLookups(BaseList):

    _arrays = {'carrier_lookups': CarrierLookup}

    def __init__(self):
        super(CarrierLookups, self).__init__()

    @property
    def elements(self):
        return self._carrier_lookups
