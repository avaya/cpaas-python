# -*- coding: utf-8 -*-

"""
zang.domain.list.cnam_lookups
~~~~~~~~~~~~~~~~~~~
`CnamLookups` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.cnam_lookup import CnamLookup


class CnamLookups(BaseList):

    _arrays = {'cnam_lookups': CnamLookup}

    def __init__(self):
        super(CnamLookups, self).__init__()

    @property
    def elements(self):
        return self._cnam_lookups
