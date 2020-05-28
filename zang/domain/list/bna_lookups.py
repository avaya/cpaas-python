# -*- coding: utf-8 -*-

"""
zang.domain.list.bna_lookups
~~~~~~~~~~~~~~~~~~~
`BnaLookups` model
"""
from zang.domain.list.base_list import BaseList
from zang.domain.bna_lookup import BnaLookup


class BnaLookups(BaseList):

    _arrays = {'bna_lookups': BnaLookup}

    def __init__(self):
        super(BnaLookups, self).__init__()

    @property
    def elements(self):
        return self._bna_lookups
