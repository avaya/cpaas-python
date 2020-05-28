# -*- coding: utf-8 -*-

"""
zang.domain.enums.auth_type
~~~~~~~~~~~~~~~~~~~
Module containing `AuthType` available options
"""
from enum import Enum


class AuthType(Enum):
    IP_ACL = 'IP_ACL'
    CREDENTIAL_LIST = 'CREDENTIAL_LIST'
    NO_TRAFFIC = 'no_traffic'
    IP_AND_CREDENTIAL = 'ip_and_credential'
