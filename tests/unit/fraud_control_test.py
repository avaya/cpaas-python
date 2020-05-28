import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class FraudControlTest(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.fraudControlConnector

    def test_list_fraud(self):
        TestUtil.start('FraudControlTest', 'listFraudControlResources')
        fraudControllRulesList = self.connector.listFraudControlResources(
            0, 22)
        assert 'FR' == fraudControllRulesList.authorized[1].countryCode
        assert 2 == len(fraudControllRulesList.authorized)

    def test_block_destination(self):
        TestUtil.start('FraudControlTest', 'blockDestination')
        fraudControlRule = self.connector.blockDestination(
            'HR', False, True, False)
        self.checkRule(fraudControlRule)

    def test_whitelist_destination(self):
        TestUtil.start('FraudControlTest', 'whitelistDestination')
        fraudControlRule = self.connector.whitelistDestination(
            'HR', False, True, False)
        self.checkRule(fraudControlRule)

    def test_authorize_destination(self):
        TestUtil.start('FraudControlTest', 'authorizeDestination')
        fraudControlRule = self.connector.authorizeDestination(
            'HR', False, True, False)
        self.checkRule(fraudControlRule)

    def test_extend_destination_authorization(self):
        TestUtil.start('FraudControlTest', 'extendDestinationAuthorization')
        fraudControlRule = self.connector.extendDestinationAuthorization('HR')
        self.checkRule(fraudControlRule)

    def checkRule(self, rule):
        assert rule.sid == 'TestFraudControlRuleSid'
