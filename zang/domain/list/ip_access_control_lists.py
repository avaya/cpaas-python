# -*- coding: utf-8 -*-

"""
zang.domain.list.ip_access_control_lists
~~~~~~~~~~~~~~~~~~~
`IpAccessControlLists` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.ip_access_control_list import IpAccessControlList


class IpAccessControlLists(BaseList):

    _arrays = {'ip_access_control': IpAccessControlList}

    def __init__(self):
        super(IpAccessControlLists, self).__init__()

    @property
    def elements(self):
        return self._ip_access_control
