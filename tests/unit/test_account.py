import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestAccount(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.accountsConnector = connectorFactory.accountsConnector

    def test_view(self):
        TestUtil.start('AccountsTest', 'viewAccount')
        account = self.accountsConnector.viewAccount()
        assert account.friendlyName == 'friendlyname1'

    def test_update(self):
        TestUtil.start('AccountsTest', 'updateAccount')
        self.accountsConnector.updateAccount('friendlyname1')

    def tearDown(self):
        pass
