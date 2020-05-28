import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.log_level import LogLevel

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestNotifications(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.notificationsConnector

    def test_view_notification(self):
        TestUtil.start('NotificationsTest', 'viewNotification')
        self.connector.viewNotification('TestNotificationSid')

    def test_list_notification(self):
        TestUtil.start('NotificationsTest', 'listNotifications')
        self.connector.listNotifications(LogLevel.INFO, 0, 33)
