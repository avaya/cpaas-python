# -*- coding: utf-8 -*-

"""
zang.connectors.sip_domains_connector
~~~~~~~~~~~~

Used for all forms of communication with the Sip Domains endpoint of the
    Zang REST API.
see ConnectorFactory
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.domain import Domain
from zang.domain.list.domains import Domains

from zang.domain.credentials_list import CredentialsList
from zang.domain.list.credentials_lists import CredentialsLists

from zang.domain.ip_access_control_list import IpAccessControlList
from zang.domain.list.ip_access_control_lists import IpAccessControlLists


class SipDomainsConnector(BaseConnector):
    """
    Used for all forms of communication with the `SIP Domains` endpoint
        of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(SipDomainsConnector, self).__init__(executor)

    def viewDomain(self, domainSid):
        """
        Shows information about a domain

        :rtype: Information about the domain
        :raises: ZangException
        """
        domain = self._executor.read(('SIP', 'Domains', domainSid), Domain)
        return domain

    def listDomains(self):
        """
        Lists available domains

        :rtype: A list of available domains
        :raises: ZangException
        """
        domains = self._executor.read(('SIP', 'Domains'), Domains)
        return domains

    def createDomain(
            self,
            domainName,
            friendlyName=None,
            voiceUrl=None,
            voiceMethod=None,
            voiceFallbackUrl=None,
            voiceFallbackMethod=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            voiceStatusCallback=None,
            voiceStatusCallbackMethod=None,):
        """
        Create a domain.

        :param domainName: An address on TelAPI uniquely associated with your
            account and through which all your SIP traffic is routed.
        :type str
        :param friendlyName: (optional) A human-readable name associated with
            this domain.
        :type str
        :param voiceUrl: (optional) The URL requested when a call is received
            by your domain.
        :type str
        :param voiceMethod: (optional) The HTTP method used when requesting
            the VoiceUrl.
        :type .domain.enums.HttpMethod
        :param voiceFallbackUrl: (optional) The URL requested if the VoiceUrl
            fails.
        :type str
        :param voiceFallbackMethod: (optional) The HTTP method used when
            requesting the VoiceFallbackUrl.
        :type .domain.enums.HttpMethod
        :param heartbeatUrl: (optional) URL that can be requested every 60
            seconds during the call to notify of elapsed time and pass other
            general information.
        :type str
        :param heartbeatMethod:POST (optional) Specifies the HTTP method used
            to request HeartbeatUrl.
        :type .domain.enums.HttpMethod
        :param voiceStatusCallback: (optional) The URL that TelAPI will use to
            send you status notifications regarding your SIP call.
        :type str
        :param voiceStatusCallbackMethod: (optional) The HTTP method used when
            requesting the VoiceStatusCallback.
        :type .domain.enums.HttpMethod

        :rtype: The created Domain
        :raises: ZangException
        """
        bodyParams = {
            'DomainName': domainName,
            'FriendlyName': friendlyName,
            'VoiceUrl': voiceUrl,
            'VoiceMethod': voiceMethod,
            'VoiceFallbackUrl': voiceFallbackUrl,
            'VoiceFallbackMethod': voiceFallbackMethod,
            'HeartbeatUrl': heartbeatUrl,
            'HeartbeatMethod': heartbeatMethod,
            'VoiceStatusCallback': voiceStatusCallback,
            'VoiceStatusCallbackMethod': voiceStatusCallbackMethod,
        }
        data = flatDict(bodyParams)
        domain = self._executor.create(('SIP', 'Domains'), Domain, data)
        return domain

    def updateDomain(
            self,
            domainSid,
            friendlyName=None,
            voiceUrl=None,
            voiceMethod=None,
            voiceFallbackUrl=None,
            voiceFallbackMethod=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            voiceStatusCallback=None,
            voiceStatusCallbackMethod=None,):
        """
        Update a domain.

        :param domainSid: Domain SID
        :type str
        :param FriendlyName: (optional) A human-readable name associated with
            this domain.
        :type str
        :param VoiceUrl: (optional) The URL requested when a call is received
            by your domain.
        :type str
        :param VoiceMethod:  (optional) The HTTP method used when requesting
            the VoiceUrl.
        :type .domain.enums.HttpMethod
        :param VoiceFallbackUrl: (optional) The URL requested if the VoiceUrl
            fails.
        :type str
        :param VoiceFallbackMethod: (optional) The HTTP method used when
            requesting the VoiceFallbackUrl.
        :type .domain.enums.HttpMethod
        :param HeartbeatUrl: (optional) URL that can be requested every 60
            seconds during the call to notify of elapsed time and pass other
            general information.
        :type str
        :param HeartbeatMethod: POST (optional) Specifies the HTTP method used
            to request HeartbeatUrl.
        :type .domain.enums.HttpMethod
        :param VoiceStatusCallback: (optional) The URL that TelAPI will use to
            send you status notifications regarding your SIP call.
        :type str
        :param VoiceStatusCallbackMethod: (optional) The HTTP method used when
            requesting the VoiceStatusCallback.
        :type .domain.enums.HttpMethod

        :rtype: The updated Domain
        :raises: ZangException
        """
        bodyParams = {
            'FriendlyName': friendlyName,
            'VoiceUrl': voiceUrl,
            'VoiceMethod': voiceMethod,
            'VoiceFallbackUrl': voiceFallbackUrl,
            'VoiceFallbackMethod': voiceFallbackMethod,
            'HeartbeatUrl': heartbeatUrl,
            'HeartbeatMethod': heartbeatMethod,
            'VoiceStatusCallback': voiceStatusCallback,
            'VoiceStatusCallbackMethod': voiceStatusCallbackMethod,
        }
        data = flatDict(bodyParams)
        domain = self._executor.update(
            ('SIP', 'Domains', domainSid), Domain, data)
        return domain

    def deleteDomain(self, domainSid):
        """
        Delete a domain.

        :param domainSid: Domain SID.
        :type str

        :rtype: The deleted Domain
        :raises: ZangException
        """
        domain = self._executor.delete(('SIP', 'Domains', domainSid), Domain)
        return domain

    # Map Credentials List

    def listMappedCredentialsLists(self, domainSid):
        """
        Shows info on credential lists attached to a SIP domain.

        :param domainSid: Domain SID.
        :rtype domainSid: str

        :rtype: zang.domain.list.credentials_lists.CredentialsLists
        :raises: ZangException
        """
        credentialsLists = self._executor.read(
            ('SIP', 'Domains', domainSid, 'CredentialListMappings'),
            CredentialsLists)
        return credentialsLists

    def mapCredentialsLists(self, domainSid, credentialListSid):
        """
        Maps credentials list to a SIP domain.

        :param domainSid: Domain SID.
        :param credentialListSid: The SID of the credential list that you
            wish to associate with this domain.

        :rtype domainSid: str
        :rtype credentialListSid: str

        :rtype: zang.domain.credentials_list.CredentialsList
        :raises: ZangException
        """
        bodyParams = {
            'CredentialListSid': credentialListSid
        }
        data = flatDict(bodyParams)
        credentialsListsList = self._executor.create(
            ('SIP', 'Domains', domainSid, 'CredentialListMappings'),
            CredentialsList, data)
        return credentialsListsList

    def deleteMappedCredentialsList(self, domainSid, credentialsListSid):
        """
        Deletes a credential list mapped to some SIP domain

        :param domainSid: Domain SID.
        :param clsId: Credentials list SID

        :type domainSid: str
        :type clsId: str

        :rtype: zang.domain.credentials_list.CredentialsList
        :raises: ZangException
        """
        credentialsListsList = self._executor.delete(
            ('SIP', 'Domains', domainSid, 'CredentialListMappings',
                credentialsListSid), CredentialsList)
        return credentialsListsList

    # Map IP ACL

    def listMappedIpAccessControlLists(self, domainSid):
        """
        Shows info on IP access control lists attached to a SIP domain

        :param domainSid: Domain SID.
        :rtype domainSid: str

        :rtype: zang.domain.list.ip_access_control_lists.IpAccessControlLists
        :raises: ZangException
        """
        ipAccessControlLists = self._executor.read(
            ('SIP', 'Domains', domainSid, 'IpAccessControlListMappings'),
            IpAccessControlLists)
        return ipAccessControlLists

    def mapIpAccessControlList(self, domainSid, ipAccessControlListSid):
        """
        Maps IP access control list to a SIP domain.

        :param domainSid: Domain SID.
        :param ipAccessControlListSid: The Sid of the IP ACL that you wish
            to associate with this domain.

        :rtype domainSid: str
        :rtype ipAccessControlListSid: str

        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises: ZangException
        """
        bodyParams = {
            'IpAccessControlListSid': ipAccessControlListSid
        }
        data = flatDict(bodyParams)
        ipAccessControlList = self._executor.create(
            ('SIP', 'Domains', domainSid, 'IpAccessControlListMappings'),
            IpAccessControlList, data)
        return ipAccessControlList

    def deleteMappedIpAccessControlList(self, domainSid, alsId):
        """
        Detaches an IP access control list from a SIP domain

        :param domainSid: Domain SID.
        :param alsId: IP access control list SID.

        :type domainSid: str
        :type alsId: str

        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises: ZangException
        """
        ipAccessControlList = self._executor.delete(
            ('SIP', 'Domains', domainSid, 'IpAccessControlListMappings',
                alsId), IpAccessControlList)
        return ipAccessControlList
