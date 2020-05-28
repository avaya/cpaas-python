# -*- coding: utf-8 -*-

"""
zang.connectors.accounts_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Accounts` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.account import Account


class AccountsConnector(BaseConnector):
    """
    Used for all forms of communication with the `Application Clients`
        endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(AccountsConnector, self).__init__(executor)

    def viewAccount(self):
        """
        See all the information associated with an account.

        :return: `Account` object
        :rtype: zang.domain.account.Account
        :raises ZangException:
        """
        sid = self._executor.configuration.sid
        account = self._executor.read(('Accounts', sid), Account)
        return account

    def updateAccount(self, friendlyName):
        """
        Updates account information.

        :param friendlyName: The custom alias for your account.
        :type friendlyName: str

        :return: Updated `Account` object
        :rtype: zang.domain.account.Account
        :raises ZangException:
        """
        sid = self._executor.configuration.sid
        bodyParams = {
            'FriendlyName': friendlyName
        }
        data = flatDict(bodyParams)
        self._executor.update(('Accounts', sid), Account, data)
