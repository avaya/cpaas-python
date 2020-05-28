# -*- coding: utf-8 -*-

"""
zang.connectors.accounts_connector
~~~~~~~~~~~~~~~~~~~
This module contains methods for communication with the ApplicationClients
REST endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.list.application_clients import ApplicationClients
from zang.domain.application_client import ApplicationClient


class ApplicationClientsConnector(BaseConnector):

    """
    Used for all forms of communication with the `Application Clients` endpoint
        of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(ApplicationClientsConnector, self).__init__(executor)

    def listApplicationClients(self, applicationSid):
        """
        Lists available application clients.

        :param applicationSid: Application SID of the client
        :type applicationSid: str

        :return: List of available Application Clients
        :rtype: zang.domain.list.ApplicationClients
        :raises ZangException:
        """
        applicationClients = self._executor.read(
            ('Applications', applicationSid, 'Clients'), ApplicationClients)
        return applicationClients

    def createApplicationClient(self, applicationSid, nickName):
        """
        Creates a new application client for your application

        :param applicationSid: Application SID of the client
        :type applicationSid: str

        :param nickname: Nickname for the new cliend
        :type nickName: str

        :return: The created ApplicationClient
        :rtype: zang.domain.ApplicationClient
        :raises ZangException:
        """
        bodyParams = {'Nickname': nickName}
        data = flatDict(bodyParams)
        applicationClient = self._executor.create(
            ('Applications', applicationSid, 'Clients', 'Tokens'),
            ApplicationClient, data)
        return applicationClient

    def viewApplicationClient(self, applicationSid, clientSid):
        """
        View all information about an application client.

        :param applicationSid: Application SID of the client
        :type applicationSid: str

        :return: Information about the Application Client
        :rtype: zang.domain.ApplicationClient
        :raises ZangException:
        """
        applicationClient = self._executor.read(
            ('Applications', applicationSid, 'Clients', clientSid),
            ApplicationClient)
        return applicationClient
