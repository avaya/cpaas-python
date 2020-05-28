# -*- coding: utf-8 -*-

"""
zang.connectors.ip_access_control_lists_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `IpAccessControlLists` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.ip_access_control_list import IpAccessControlList
from zang.domain.list.ip_access_control_lists import IpAccessControlLists

from zang.domain.ip_address import IpAddress
from zang.domain.list.ip_addresses import IpAddresses


class IpAccessControlListsConnector(BaseConnector):
    """
    Used for all forms of communication with the `IpAccessControlLists`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewIpAcl(self, ipAccessControlListSid):
        """
        View information for IP access control list

        :param ipAccessControlListSid: IP access control list SID.
        :type recordingSid: str

        :return: `IpAccessControlList` object
        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises ZangException:
        """
        ipAccessControlList = self._executor.read(
            ('SIP', 'IpAccessControlLists', ipAccessControlListSid),
            IpAccessControlList)
        return ipAccessControlList

    def listIpAcls(self, page=None, pageSize=None):
        """
        List all IP access control lists associated with a particular account.

        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type page: int
        :type pageSize: int

        :return: `IpAccessControlLists` object
        :rtype: zang.domain.list.ip_access_control_lists.IpAccessControlLists
        :raises ZangException:
        """
        queryParams = {
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        ipAccessControlLists = self._executor.read(
            ('SIP', 'IpAccessControlLists'), IpAccessControlLists, params)
        return ipAccessControlLists

    def createIpAcl(self, friendlyName):
        """
        Create IP access control list

        :param friendlyName: A human-readable name associated with this IP ACL.
        :type page: str

        :return: `IpAccessControlList` object
        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName,
        }
        data = flatDict(bodyParams)
        ipAccessControlList = self._executor.create(
            ('SIP', 'IpAccessControlLists'), IpAccessControlList, data)
        return ipAccessControlList

    def updateIpAcl(self, ipAccessControlListSid, friendlyName):
        """
        Updates information for IP access control list

        :param ipAccessControlListSid: IP access control list SID.
        :param friendlyName: A human-readable name associated with this IP ACL.

        :type recordingSid: str
        :type page: str

        :return: `IpAccessControlList` object
        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName,
        }
        data = flatDict(bodyParams)
        ipAccessControlList = self._executor.update(
            ('SIP', 'IpAccessControlLists', ipAccessControlListSid),
            IpAccessControlList, data)
        return ipAccessControlList

    def deleteIpAcl(self, ipAccessControlListSid):
        """
        Deletes IP access control list

        :param ipAccessControlListSid: IP access control list SID.
        :type recordingSid: str

        :return: `IpAccessControlList` object
        :rtype: zang.domain.ip_access_control_list.IpAccessControlList
        :raises ZangException:
        """
        ipAccessControlList = self._executor.delete(
            ('SIP', 'IpAccessControlLists', ipAccessControlListSid),
            IpAccessControlList)
        return ipAccessControlList

    def viewAclIp(self, aclSid, ipSid):
        """
        View information on IP access control list IP address.

        :param aclSid: IP access control list SID.
        :param ipSid: Access control list IP address SID.

        :type aclSid: str
        :type ipSid: str

        :return: `IpAddress` object
        :rtype: zang.domain.ip_address.IpAddress
        :raises ZangException:
        """
        ipAddress = self._executor.read(
            ('SIP', 'IpAccessControlLists', aclSid, 'IpAddresses', ipSid),
            IpAddress)
        return ipAddress

    def listAclIps(self, aclSid):
        """
        Lists IP addresses attached to some IP access control list.

        :param aclSid: IP access control list SID.
        :type aclSid: str

        :return: `IpAddresses` object
        :rtype: zang.domain.list.ip_addresses.IpAddresses
        :raises ZangException:
        """
        ipAddresses = self._executor.read(
            ('SIP', 'IpAccessControlLists', aclSid, 'IpAddresses'),
            IpAddresses)
        return ipAddresses

    def addAclIp(self, aclSid, friendlyName=None, ipAddress=None):
        """
        Add new IP for access control lis

        :param aclSid: IP access control list SID.
        :param friendlyName: A human-readable name associated with this IP ACL.
        :param ipAddress: An IP address from which you wish to accept traffic.
            At this time, only IPv4 supported.

        :type aclSid: str
        :type friendlyName: str
        :type ipAddress: str

        :return: `IpAddress` object
        :rtype: zang.domain.ip_address.IpAddress
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName,
            'IpAddress': ipAddress,
        }
        data = flatDict(bodyParams)
        ipAddress = self._executor.create(
            ('SIP', 'IpAccessControlLists', aclSid, 'IpAddresses'), IpAddress,
            data)
        return ipAddress

    def updateAclIp(self, aclSid, ipSid, friendlyName=None, ipAddress=None):
        """
        Updates IP address for IP access control list

        :param aclSid: IP access control list SID.
        :param ipSid: Access control list IP address SID.
        :param friendlyName: A human-readable name associated with this IP ACL.
        :param ipAddress: An IP address from which you wish to accept traffic.
            At this time, only IPv4 supported.

        :type aclSid: str
        :type ipSid: str
        :type friendlyName: str
        :type ipAddress: str

        :return: `IpAddress` object
        :rtype: zang.domain.ip_address.IpAddress
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName,
            'IpAddress': ipAddress,
        }
        data = flatDict(bodyParams)
        ipAddress = self._executor.update(
            ('SIP', 'IpAccessControlLists', aclSid, 'IpAddresses', ipSid),
            IpAddress, data)
        return ipAddress

    def deleteAclIp(self, aclSid, ipSid):
        """
        Deletes IP address from IP access control list.

        :param aclSid: IP access control list SID.
        :param ipSid: Access control list IP address SID.

        :type aclSid: str
        :type ipSid: str

        :return: `IpAddress` object
        :rtype: zang.domain.ip_address.IpAddress
        :raises ZangException:
        """
        ipAddress = self._executor.delete(
            ('SIP', 'IpAccessControlLists', aclSid, 'IpAddresses', ipSid),
            IpAddress)
        return ipAddress
