# -*- coding: utf-8 -*-

"""
zang.domain.list.notifications
~~~~~~~~~~~~~~~~~~~
`Notifications` model
"""
from zang.domain.list.base_list import BaseList
from zang.domain.notification import Notification


class Notifications(BaseList):

    _arrays = {'notifications': Notification}

    def __init__(self):
        super(Notifications, self).__init__()

    @property
    def elements(self):
        return self._notifications
