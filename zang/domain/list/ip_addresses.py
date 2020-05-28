# -*- coding: utf-8 -*-

"""
zang.domain.list.ip_access_control_lists
~~~~~~~~~~~~~~~~~~~
`IpAddresses` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.ip_address import IpAddress


class IpAddresses(BaseList):

    _arrays = {'ip_addresses': IpAddress}

    def __init__(self):
        super(IpAddresses, self).__init__()

    def __repr__(self):
        return '<IpAddresses at 0x%x>' % (id(self))

    @property
    def elements(self):
        return self._ip_addresses
