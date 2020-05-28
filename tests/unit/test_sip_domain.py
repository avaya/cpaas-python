import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.auth_type import AuthType

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestSipDomain(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.sipDomainsConnector

    def test_view_domain(self):
        TestUtil.start('SipDomainsTest', 'viewDomain')
        obj = self.connector.viewDomain('TestDomainSid')
        self.checkDomain(obj)

    def test_list_domains(self):
        TestUtil.start('SipDomainsTest', 'listDomains')
        obj = self.connector.listDomains()
        assert len(obj.elements) == 2
        self.checkDomain(obj.elements[0])

    def test_create_domain(self):
        TestUtil.start('SipDomainsTest', 'createDomain')
        self.connector.createDomain(
            domainName='mydomain.com',
            friendlyName='MyDomain',
            voiceUrl='VoiceUrl',
            voiceMethod=HttpMethod.POST,
            voiceFallbackUrl='VoiceFallbackUrl',
            voiceFallbackMethod=HttpMethod.GET,
            heartbeatUrl='HeartbeatUrl',
            heartbeatMethod=HttpMethod.POST,
            voiceStatusCallback='VoiceStatusCallback',
            voiceStatusCallbackMethod=HttpMethod.GET)

    def test_update_domain(self):
        TestUtil.start('SipDomainsTest', 'updateDomain')
        self.connector.updateDomain(
            'TestDomainSid',
            friendlyName='MyDomain',
            voiceUrl='VoiceUrl',
            voiceMethod=HttpMethod.POST,
            voiceFallbackUrl='VoiceFallbackUrl',
            voiceFallbackMethod=HttpMethod.GET,
            heartbeatUrl='HeartbeatUrl',
            heartbeatMethod=HttpMethod.POST,
            voiceStatusCallback='VoiceStatusCallback',
            voiceStatusCallbackMethod=HttpMethod.GET)

    def test_delete_domain(self):
        TestUtil.start('SipDomainsTest', 'deleteDomain')
        self.connector.deleteDomain('TestDomainSid')

    def checkDomain(self, domain):
        assert domain.authType == AuthType.IP_AND_CREDENTIAL
        assert domain.voiceHeartbeatCallback is None
        assert domain.friendlyName == 'MyDomain2'
        assert domain.domainName == 'mytestdomain.com'

    # Map Credentials List

    def test_list_mapped_credentials_list(self):
        TestUtil.start('SipDomainsTest', 'listMappedCredentialsList')
        obj = self.connector.listMappedCredentialsLists('TestDomainSid')
        assert len(obj.elements) == obj.total
        assert obj.elements[0].friendlyName == 'MyCredentialsList'

    def test_map_credentials_list(self):
        TestUtil.start('SipDomainsTest', 'mapCredentialsList')
        obj = self.connector.mapCredentialsLists(
            'TestDomainSid', 'TestCredentialsListSid')
        self.checkCredentialsLlist(obj)

    def test_delete_mapped_credentials_list(self):
        TestUtil.start('SipDomainsTest', 'deleteMappedCredentialsList')
        obj = self.connector.deleteMappedCredentialsList(
            'TestDomainSid', 'TestCredentialsListSid')
        self.checkCredentialsLlist(obj)

    def checkCredentialsLlist(self, credentialsList):
        assert credentialsList.friendlyName == 'MyCredentialsList2'
        assert credentialsList.sid == 'CL7c88908457d7a68609b644e88ec80198'

    # Map IP ACL

    def test_list_mapped_ip_acls(self):
        TestUtil.start('SipDomainsTest', 'listMappedIpAcls')
        obj = self.connector.listMappedIpAccessControlLists('TestDomainSid')
        assert len(obj.elements) == obj.total
        assert obj.pageSize == 100
        assert obj.elements[0].friendlyName == 'MyAclList'

    def test_map_ip_acl(self):
        TestUtil.start('SipDomainsTest', 'mapIpAcl')
        obj = self.connector.mapIpAccessControlList(
            'TestDomainSid', 'TestIpAccessControlListSid')
        self.checkIpAcl(obj)

    def test_delete_ip_acl(self):
        TestUtil.start('SipDomainsTest', 'deleteIpAcl')
        obj = self.connector.deleteMappedIpAccessControlList(
            'TestDomainSid', 'TestIpAccessControlListSid')
        self.checkIpAcl(obj)

    def checkIpAcl(self, ipAcl):
        assert ipAcl.friendlyName == 'MyAclList2'
        assert ipAcl.ipAddressesCount == 0
