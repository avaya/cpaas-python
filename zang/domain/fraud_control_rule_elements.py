# -*- coding: utf-8 -*-

"""
zang.domain.fraud_control_rule_elements
~~~~~~~~~~~~~~~~~~~
`FraudControlRuleElements` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.fraud_control_rule_element import FraudControlRuleElement


class FraudControlRuleElements(BaseList):

    _arrays = {'frauds': FraudControlRuleElement}

    def __init__(self):
        super(FraudControlRuleElements, self).__init__()

    @property
    def elements(self):
        """:rtype: List of FraudControlRuleElement elements"""
        return self._frauds

    @property
    def authorized(self):
        """:rtype: List of authorized FraudControlRule elements"""
        authorized_ = []
        for element in self._frauds:
            if element.authorized:
                authorized_.append(element.authorized)
        return authorized_

    @property
    def blocked(self):
        """:rtype: List of blocked FraudControlRule elements"""
        blocked_ = []
        for element in self._frauds:
            if element.blocked:
                blocked_.append(element.blocked)
        return blocked_

    @property
    def whitelisted(self):
        """:rtype: List of whitelisted FraudControlRule elements"""
        whitelisted_ = []
        for element in self._frauds:
            if element.whitelisted:
                whitelisted_.append(element.whitelisted)
        return whitelisted_
