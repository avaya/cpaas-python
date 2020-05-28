import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.presence_status import PresenceStatus

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestApplicationClients(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.applicationClientsConnector

    def test_view_application_client(self):
        TestUtil.start('ApplicationClientsTest', 'viewApplicationClient')
        applicationClient = self.connector.viewApplicationClient(
            'TestApplicationSid', 'TestApplicationClientSid')
        self.check_application_client(applicationClient)

    def test_list_application_client(self):
        TestUtil.start('ApplicationClientsTest', 'listApplicationClients')
        applicationClients = self.connector.listApplicationClients(
            'TestApplicationSid')
        assert len(applicationClients.elements) == 1
        applicationClient = applicationClients.elements[0]
        self.check_application_client(applicationClient)

    def test_create_application_client(self):
        TestUtil.start('ApplicationClientsTest', 'createApplicationClient')
        applicationClient = self.connector.createApplicationClient(
            'TestApplicationSid', 'MyApplicationClient')
        self.check_application_client(applicationClient)

    def check_application_client(self, applicationClient):
        assert applicationClient.sid == 'TestApplicationClientSid'
        assert applicationClient.nickname == 'MyApplicationClient'
        assert applicationClient.remoteIp == '10.0.0.1'
        assert applicationClient.presenceStatus == PresenceStatus.INIT
