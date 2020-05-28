# -*- coding: utf-8 -*-

"""
zang.connectors.sip_credentials_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `SIP Credentials` endpoint
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.credential import Credential
from zang.domain.list.credentials import Credentials

from zang.domain.credentials_list import CredentialsList
from zang.domain.list.credentials_lists import CredentialsLists


class SipCredentialsConnector(BaseConnector):
    """
    Used for all forms of communication with the `SIP Credentials` endpoint
        of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewCredentialsList(self, clsId):
        """
        View info on SIP domain credentials list.

        :param clsId: Credentials list SID.
        :type clsId: str

        :return: Information about the credentials list.
        :rtype: zang.domain.credentials_list.CredentialsList
        :raises ZangException:
        """
        credentialsList = self._executor.read(
            ('SIP', 'CredentialLists', clsId), CredentialsList)
        return credentialsList

    def listCredentialsLists(self):
        """
        Show info on SIP domain credentials lists.

        :return: A list of available credentials lists.
        :rtype: zang.domain.credentials_lists.CredentialsLists
        :raises ZangException:
        """
        credentialsLists = self._executor.read(
            ('SIP', 'CredentialLists'), CredentialsLists)
        return credentialsLists

    def createCredentialsList(self, friendlyName):
        """
        Creates SIP domain credentials list.

        :param friendlyName: A human readable name for this credential list.
        :type friendlyName: str

        :return: The created credentials list.
        :rtype: zang.domain.credentials_list.CredentialsList
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName
        }
        data = flatDict(bodyParams)
        credential = self._executor.create(
            ('SIP', 'CredentialLists'), CredentialsList, data)
        return credential

    def updateCredentialsList(self, clsId, friendlyName):
        """
        Updates info for credentials list.

        :param clsId: Credentials list SID.
        :param friendlyName: A human readable name for this credential list.

        :type clsId: str
        :type friendlyName: str

        :return: The updated credentials list.
        :rtype: zang.domain.credentials_list.CredentialsList
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName
        }
        data = flatDict(bodyParams)
        credentialsList = self._executor.update(
            ('SIP', 'CredentialLists', clsId), CredentialsList, data)
        return credentialsList

    def deleteCredentialsList(self, clsId):
        """
        Deletes SIP domain credentials list.

        :param clsId: Credentials list SID.
        :type clsId: str

        :return: The deleted credentials list.
        :rtype: zang.domain.credentials_list.CredentialsList
        :raises ZangException:
        """
        credentialsList = self._executor.delete(
            ('SIP', 'CredentialLists', clsId), CredentialsList)
        return credentialsList

    # CREDENTIAL

    def viewCredential(self, clsId, credentialSid):
        """
        View SIP domain credentials information.

        :param clsId: Credentials list SID.
        :param credentialSid: Credential SID.

        :type clsId: str
        :type credentialSid: str

        :return: Information about the credential.
        :rtype: zang.domain.credential.Credential
        :raises ZangException:
        """
        credential = self._executor.read(
            ('SIP', 'CredentialLists', clsId, 'Credentials', credentialSid),
            Credential)
        return credential

    def listCredentials(self, clsId):
        """
        Show info on all credentials attached to a particular credentials list.

        :param clsId: Credentials list SID.
        :type clsId: str

        :return: A list of available credentials.
        :rtype: zang.domain.credentials.Credentials
        :raises ZangException:
        """
        credentials = self._executor.read(
            ('SIP', 'CredentialLists', clsId, 'Credentials'), Credentials)
        return credentials

    def createCredential(self, clsId, username, password):
        """
        Create SIP domain credentials.

        :param clsId: Credentials list SID.
        :param username: The username used to identify this credential.
        :param password: The password used to authenticate this credential.

        :type clsId: str
        :type username: str
        :type password: str

        :return: The created Credential.
        :rtype: zang.domain.credential.Credential
        :raises ZangException:
        """
        bodyParams = {
            'Username': username,
            'Password': password,
        }
        data = flatDict(bodyParams)
        credential = self._executor.create(
            ('SIP', 'CredentialLists', clsId, 'Credentials'), Credential, data)
        return credential

    def updateCredential(self, clsId, credentialSid, password):
        """
        Updates SIP domain credentials

        :param clsId: Credentials list SID.
        :param credentialSid: Credential SID.
        :param password: The password used to authenticate this credential.

        :type clsId: str
        :type credentialSid: str
        :type password: str

        :return: The updated Credential.
        :rtype: zang.domain.credential.Credential
        :raises ZangException:
        """
        bodyParams = {
            'Password': password,
        }
        data = flatDict(bodyParams)
        credential = self._executor.update(
            ('SIP', 'CredentialLists', clsId, 'Credentials', credentialSid),
            Credential, data)
        return credential

    def deleteCredential(self, clsId, credentialSid):
        """
        Deletes SIP domain credentials.

        :param clsId: Credentials list SID.
        :param credentialSid: Credential SID.

        :type clsId: str
        :type credentialSid: str

        :return: The deleted Credential.
        :rtype: zang.domain.credential.Credential
        :raises ZangException:
        """
        credential = self._executor.delete(
            ('SIP', 'CredentialLists', clsId, 'Credentials', credentialSid),
            Credential)
        return credential
