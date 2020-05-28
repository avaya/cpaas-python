# -*- coding: utf-8 -*-

"""
zang.connectors.fraud_control_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `FraudControlConnector` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.fraud_control_rule_element import FraudControlRuleElement
from zang.domain.fraud_control_rule_elements import FraudControlRuleElements


class FraudControlConnector(BaseConnector):
    """
    Used for all forms of communication with the `FraudControlConnector`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def blockDestination(
            self,
            countryCode,
            mobileEnabled=None,
            landlineEnabled=None,
            smsEnabled=None,):
        """
        Restricts outbound calls and sms messages to some destination.

        :param countryCode:Country code.
        :param mobileEnabled: (optional) Mobile status for the destination.
            If false,all mobile call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param landlineEnabled: (optional) Landline status for the destination.
            If false, all landline call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param smsEnabled: (optional) SMS status for the destination. If false,
            all SMS activity will be rejected or disabled. Allowed values are
            "true" and "false".

        :type countryCode: str
        :type mobileEnabled: bool
        :type landlineEnabled: bool
        :type smsEnabled: bool

        :return: `FraudControlRuleElement` object
        :rtype: zang.domain.fraud_control_rule_element.FraudControlRuleElement
        :raises ZangException:
        """
        bodyParams = {
            'MobileEnabled': mobileEnabled,
            'LandlineEnabled': landlineEnabled,
            'SmsEnabled': smsEnabled,
        }
        data = flatDict(bodyParams)
        fraudControlRuleElement = self._executor.create(
            ('Fraud', 'Block', countryCode), FraudControlRuleElement, data)
        return fraudControlRuleElement.blocked

    def authorizeDestination(
            self,
            countryCode,
            mobileEnabled=None,
            landlineEnabled=None,
            smsEnabled=None,):
        """
        Authorizes previously blocked destination for outbound calls and sms
        messages.

        :param countryCode:Country code.
        :param mobileEnabled: (optional) Mobile status for the destination.
            If false,all mobile call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param landlineEnabled: (optional) Landline status for the destination.
            If false, all landline call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param smsEnabled: (optional) SMS status for the destination. If false,
            all SMS activity will be rejected or disabled. Allowed values are
            "true" and "false".

        :type countryCode: str
        :type mobileEnabled: bool
        :type landlineEnabled: bool
        :type smsEnabled: bool

        :return: `FraudControlRuleElement` object
        :rtype: zang.domain.fraud_control_rule_element.FraudControlRuleElement
        :raises ZangException:
        """
        bodyParams = {
            'MobileEnabled': mobileEnabled,
            'LandlineEnabled': landlineEnabled,
            'SmsEnabled': smsEnabled,
        }
        data = flatDict(bodyParams)
        fraudControlRuleElement = self._executor.create(
            ('Fraud', 'Authorize', countryCode), FraudControlRuleElement,
            data)
        return fraudControlRuleElement.authorized

    def whitelistDestination(
            self,
            countryCode,
            mobileEnabled=None,
            landlineEnabled=None,
            smsEnabled=None,):
        """
        Permanently authorizes destination that may have been blocked by our
        automated fraud detection system

        :param countryCode:Country code.
        :param mobileEnabled: (optional) Mobile status for the destination.
            If false,all mobile call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param landlineEnabled: (optional) Landline status for the destination.
            If false, all landline call activity will be rejected or disabled.
            Allowed values are "true" and "false".
        :param smsEnabled: (optional) SMS status for the destination. If false,
            all SMS activity will be rejected or disabled. Allowed values are
            "true" and "false".

        :type countryCode: str
        :type mobileEnabled: bool
        :type landlineEnabled: bool
        :type smsEnabled: bool

        :return: `FraudControlRuleElement` object
        :rtype: zang.domain.fraud_control_rule_element.FraudControlRuleElement
        :raises ZangException:
        """
        bodyParams = {
            'MobileEnabled': mobileEnabled,
            'LandlineEnabled': landlineEnabled,
            'SmsEnabled': smsEnabled,
        }
        data = flatDict(bodyParams)
        fraudControlRuleElement = self._executor.create(
            ('Fraud', 'Whitelist', countryCode), FraudControlRuleElement, data)
        return fraudControlRuleElement.whitelisted

    def extendDestinationAuthorization(self, countryCode):
        """
        Extends a destinations authorization expiration by 30 days

        :param countryCode:Country code.
        :type countryCode: str

        :return: `FraudControlRuleElement` object
        :rtype: zang.domain.fraud_control_rule_element.FraudControlRuleElement
        :raises ZangException:
        """
        fraudControlRuleElement = self._executor.update(
            ('Fraud', 'Extend', countryCode), FraudControlRuleElement)
        return fraudControlRuleElement.authorized

    def listFraudControlResources(self, page=None, pageSize=None):
        """
        Shows information on all fraud control resources associated with some
        account.

        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type page: int
        :type pageSize: int

        :return: `FraudControlRuleElements` object
        :rtype: zang.domain.fraud_control_rule_elements.
            FraudControlRuleElements
        :raises ZangException:
        """
        queryParams = {
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        fraudControlRuleElements = self._executor.read(
            ('Fraud',), FraudControlRuleElements, params)
        return fraudControlRuleElements
