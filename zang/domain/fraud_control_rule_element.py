# -*- coding: utf-8 -*-

"""
zang.domain.fraud_control_rule_whitelisted
~~~~~~~~~~~~~~~~~~~
`FraudControlRuleElement` model
"""

from zang.domain.base_resource import BaseResource
from zang.domain.fraud_control_rule import FraudControlRule


class FraudControlRuleElement(BaseResource):

    _map = {
        'blocked': FraudControlRule,
        'authorized': FraudControlRule,
        'whitelisted': FraudControlRule,
    }

    def __init__(self):
        super(FraudControlRuleElement, self).__init__()

    @property
    def blocked(self):
        return self._blocked

    @property
    def authorized(self):
        return self._authorized

    @property
    def whitelisted(self):
        return self._whitelisted
