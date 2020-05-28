import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestSipCredentials(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.sipCredentialsConnector

    def test_view_credentials_list(self):
        TestUtil.start('SipCredentialsTest', 'viewCredentialsList')
        self.connector.viewCredentialsList('TestCredentialsListSid')

    def test_list_credentials_lists(self):
        TestUtil.start('SipCredentialsTest', 'listCredentialsLists')
        self.connector.listCredentialsLists()

    def test_create_credentials_list(self):
        TestUtil.start('SipCredentialsTest', 'createCredentialsList')
        self.connector.createCredentialsList('MyCredentialsList')

    def test_update_credentials_list(self):
        TestUtil.start('SipCredentialsTest', 'updateCredentialsList')
        self.connector.updateCredentialsList(
            'TestCredentialsListSid', 'NewCredentialsList')

    def test_delete_credentials_list(self):
        TestUtil.start('SipCredentialsTest', 'deleteCredentialsList')
        self.connector.deleteCredentialsList('TestCredentialsListSid')

    def test_view_credential(self):
        TestUtil.start('SipCredentialsTest', 'viewCredential')
        self.connector.viewCredential(
            'TestCredentialsListSid', 'TestCredentialSid')

    def test_list_credentials(self):
        TestUtil.start('SipCredentialsTest', 'listCredentials')
        self.connector.listCredentials('TestCredentialsListSid')

    def test_create_credential(self):
        TestUtil.start('SipCredentialsTest', 'createCredential')
        self.connector.createCredential(
            'TestCredentialsListSid', 'username', 'password')

    def test_update_credential(self):
        TestUtil.start('SipCredentialsTest', 'updateCredential')
        self.connector.updateCredential(
            'TestCredentialsListSid', 'TestCredentialSid', 'password')

    def test_delete_credential(self):
        TestUtil.start('SipCredentialsTest', 'deleteCredential')
        self.connector.deleteCredential(
            'TestCredentialsListSid', 'TestCredentialSid')
