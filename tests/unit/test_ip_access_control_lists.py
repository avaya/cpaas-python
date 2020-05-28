import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestIpAccessControlLists(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.ipAccessControlListsConnector

    def test_view_ip_acl(self):
        TestUtil.start('SipAclTest', 'viewIpAcl')
        ipAcl = self.connector.viewIpAcl('TestIpAccessControlListSid')
        assert ipAcl.sid == 'AL22889084490426121fee48688affbda3'
        assert ipAcl.ipAddressesCount == 0

    def test_list_ip_acls(self):
        TestUtil.start('SipAclTest', 'listIpAcls')
        ipAcl = self.connector.listIpAcls(0, 50)
        assert ipAcl.elements[0].friendlyName == 'MyAclList'

    def test_create_ip_acls(self):
        TestUtil.start('SipAclTest', 'createIpAcl')
        ipAcl = self.connector.createIpAcl('MyIpAclList')
        assert ipAcl.sid == 'AL22889084490426121fee48688affbda3'
        assert ipAcl.ipAddressesCount == 0

    def test_update_ip_acls(self):
        TestUtil.start('SipAclTest', 'updateIpAcl')
        ipAcl = self.connector.updateIpAcl(
            'TestIpAccessControlListSid', 'NewIpAclList')
        assert ipAcl.sid == 'AL22889084490426121fee48688affbda3'
        assert ipAcl.ipAddressesCount == 0

    def test_delete_ip_acls(self):
        TestUtil.start('SipAclTest', 'deleteIpAcl')
        ipAcl = self.connector.deleteIpAcl('TestIpAccessControlListSid')
        assert ipAcl.sid == 'AL22889084490426121fee48688affbda3'
        assert ipAcl.ipAddressesCount == 0

    def test_view_acl_ips(self):
        TestUtil.start('SipAclTest', 'viewAclIp')
        aclIps = self.connector.viewAclIp(
            'TestIpAccessControlListSid', 'TestIpAddressSid')
        self.check_acl_ips(aclIps)

    def test_list_acl_ipss(self):
        TestUtil.start('SipAclTest', 'listAclIps')
        aclIps = self.connector.listAclIps('TestIpAccessControlListSid')
        assert aclIps.total == 1
        assert aclIps.elements[0].friendlyName == 'MyIpAddress2'

    def test_create_acl_ipss(self):
        TestUtil.start('SipAclTest', 'addAclIp')
        aclIps = self.connector.addAclIp(
            'TestIpAccessControlListSid', 'MyIpAddress', '10.0.0.1')
        self.check_acl_ips(aclIps)

    def test_update_acl_ipss(self):
        TestUtil.start('SipAclTest', 'updateAclIp')
        aclIps = self.connector.updateAclIp(
            'TestIpAccessControlListSid', 'TestIpAddressSid', 'NewIpAddress',
            '10.0.0.2')
        self.check_acl_ips(aclIps)

    def test_delete_acl_ipss(self):
        TestUtil.start('SipAclTest', 'deleteAclIp')
        aclIps = self.connector.deleteAclIp(
            'TestIpAccessControlListSid', 'TestIpAddressSid')
        self.check_acl_ips(aclIps)

    def check_acl_ips(self, aclIps):
        assert aclIps.ipAddress == '192.168.12.12'
        assert aclIps.friendlyName == 'MyIpAddress'
