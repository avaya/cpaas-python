import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.mms_message_status import MmsMessageStatus
from zang.domain.enums.mms_direction import MmsDirection

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestMmsMessages(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.mmsMessagesConnector

    def test_send(self):
        TestUtil.start('MmsTest', 'sendMms')
        mmsMessage = self.connector.sendMmsMessage(
            to='+123456',
            mediaUrl="https://media.giphy.com/media/zZJzLrxmx5ZFS/giphy.gif", 
            from_='+654321', 
            body='This is MMS sent from Zang',
            statusCallback='callback.url',
            statusCallbackMethod=HttpMethod.GET.value)
        self.checkMessage(mmsMessage)

    def checkMessage(self, mmsMessage):
        assert mmsMessage.body == 'This is MMS sent from Zang'
        assert mmsMessage.status == MmsMessageStatus.QUEUED
        assert mmsMessage.direction == MmsDirection.OUTBOUND_API
