import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestIncomingPhoneNumbers(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.incomingPhoneNumbersConnector

    def test_view_incoming_phone_number(self):
        TestUtil.start('IncomingPhoneNumbersTest', 'viewIncomingPhoneNumber')
        obj = self.connector.viewIncomingPhoneNumber(
            'TestIncomingPhoneNumberSid')
        assert 'http://www.zang.io/ivr/welcome/sms' == obj.smsUrl

    def test_list_incoming_phone_numbers(self):
        TestUtil.start('IncomingPhoneNumbersTest', 'listIncomingPhoneNumbers')
        self.connector.listIncomingPhoneNumbers('123', 'MyNumber', 0, 25)

    def test_purchase_incoming_phone_numbers(self):
        TestUtil.start(
            'IncomingPhoneNumbersTest', 'purchaseIncomingPhoneNumber')

        self.connector.purchaseIncomingPhoneNumber(
            friendlyName='MyNumber',
            phoneNumber='+1234',
            areaCode='123',
            voiceCallerIdLookup=True,
            voiceApplicationSid='VoiceApplicationSid',
            smsApplicationSid='SmsApplicationSid',
            voiceUrl='VoiceUrl',
            voiceMethod=HttpMethod.GET,
            voiceFallbackUrl='VoiceFallbackUrl',
            voiceFallbackMethod=HttpMethod.GET,
            smsUrl='SmsUrl',
            smsMethod=HttpMethod.GET,
            smsFallbackUrl='SmsFallbackUrl',
            smsFallbackMethod=HttpMethod.POST,
            heartbeatUrl='HeartbeatUrl',
            heartbeatMethod=HttpMethod.POST,
            statusCallback='StatusCallback',
            statusCallbackMethod=HttpMethod.POST,
            hangupCallback='HangupCallback',
            hangupCallbackMethod=HttpMethod.POST,)

    def test_update_incoming_phone_numbers(self):
        TestUtil.start(
            'IncomingPhoneNumbersTest', 'updateIncomingPhoneNumber')
        self.connector.updateIncomingPhoneNumber(
            'TestIncomingPhoneNumberSid',
            friendlyName='MyNumber',
            voiceCallerIdLookup=True,
            voiceUrl='VoiceUrl',
            voiceMethod=HttpMethod.GET,
            voiceFallbackUrl='VoiceFallbackUrl',
            voiceFallbackMethod=HttpMethod.GET,
            smsUrl='SmsUrl',
            smsMethod=HttpMethod.GET,
            smsFallbackUrl='SmsFallbackUrl',
            smsFallbackMethod=HttpMethod.POST,
            heartbeatUrl='HeartbeatUrl',
            heartbeatMethod=HttpMethod.POST,
            statusCallback='StatusCallback',
            statusCallbackMethod=HttpMethod.POST,
            hangupCallback='HangupCallback',
            hangupCallbackMethod=HttpMethod.POST),

    def test_delete_incoming_phone_numbers(self):
        TestUtil.start(
            'IncomingPhoneNumbersTest', 'deleteIncomingPhoneNumber')
        self.connector.deleteIncomingPhoneNumber('TestIncomingPhoneNumberSid')
