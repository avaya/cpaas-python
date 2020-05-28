import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.sms_message_status import SmsMessageStatus
from zang.domain.enums.sms_direction import SmsDirection

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestSmsMessages(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.smsMessagesConnector

    def test_view(self):
        TestUtil.start('SmsTest', 'viewSms')
        smsMessage = self.connector.viewSmsMessage('TestSmsSid')
        self.checkMessage(smsMessage)

    def test_list(self):
        TestUtil.start('SmsTest', 'listSms')
        smsMessages = self.connector.listSmsMessages(
            '+123456', page=0, pageSize=10)
        cnt = 0
        fromList = None
        for smsMessage in smsMessages.elements:
            cnt += 1
            fromList = smsMessage
        assert cnt == 2
        assert 1 == smsMessages.numPages
        self.checkMessage(fromList)

    def test_send(self):
        TestUtil.start('SmsTest', 'sendSms')
        smsMessage = self.connector.sendSmsMessage(
            to='+123456', from_='+654321', body='test from java',
            statusCallback='callback.url',
            statusCallbackMethod=HttpMethod.GET.value, allowMultiple=False)
        self.checkMessage(smsMessage)

    def checkMessage(self, smsMessage):
        assert smsMessage.body == 'test from java'
        assert smsMessage.status == SmsMessageStatus.SENT
        assert smsMessage.direction == SmsDirection.OUTBOUND_API
        assert smsMessage.price == 0.0616
