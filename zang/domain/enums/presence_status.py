# -*- coding: utf-8 -*-

"""
zang.domain.enums.presence_status
~~~~~~~~~~~~~~~~~~~
Module containing `PresenceStatus` available options
"""
from enum import Enum


class PresenceStatus(Enum):
    INIT = 'init'
    IDLE = 'idle'
    LOGGED_IN = 'loggedin'
    LOGGED_OUT = 'loggedout'
