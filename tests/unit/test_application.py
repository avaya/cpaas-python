import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod
from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestApplication(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.applicationsConnector = \
            connectorFactory.applicationsConnector

    def test_view(self):
        TestUtil.start('ApplicationsTest', 'viewApplication')
        application = self.applicationsConnector.viewApplication(
            'TestApplicationSid')
        self._checkApplication(application)

    def test_list(self):
        TestUtil.start('ApplicationsTest', 'listApplications')
        applications = self.applicationsConnector.listApplications(
            "TestApplication", 0, 10)
        assert len(applications.elements) == 1
        self._checkApplication(applications.elements[0])

    def test_update(self):
        TestUtil.start('ApplicationsTest', 'updateApplication')
        application = self.applicationsConnector.updateApplication(
            "TestApplicationSid",
            "TestApplication",
            "voiceUrl",
            HttpMethod.POST,
            "voiceFallbackUrl",
            HttpMethod.GET,
            True,
            "smsUrl",
            HttpMethod.POST,
            "smsFallbackUrl",
            HttpMethod.GET,
            "heartbeatUrl",
            HttpMethod.GET,
            "statusCallback",
            HttpMethod.POST,
            "hangupCallback",
            HttpMethod.GET)
        self._checkApplication(application)

    def test_create(self):
        TestUtil.start('ApplicationsTest', 'createApplication')
        application = self.applicationsConnector.createApplication(
            friendlyName="TestApplication",
            voiceUrl="voiceUrl",
            voiceMethod=HttpMethod.POST,
            voiceFallbackUrl="voiceFallbackUrl",
            voiceFallbackMethod=HttpMethod.GET,
            voiceCallerIdLookup=True,
            smsUrl="smsUrl",
            smsMethod=HttpMethod.POST,
            smsFallbackUrl="smsFallbackUrl",
            smsFallbackMethod=HttpMethod.GET,
            heartbeatUrl="heartbeatUrl",
            heartbeatMethod=HttpMethod.GET,
            statusCallback="statusCallback",
            statusCallbackMethod=HttpMethod.POST,
            hangupCallback="hangupCallback",
            hangupCallbackMethod=HttpMethod.GET)
        self._checkApplication(application)

    def test_delete(self):
        TestUtil.start('ApplicationsTest', 'deleteApplication')
        application = self.applicationsConnector.deleteApplication(
            "TestApplicationSid")
        self._checkApplication(application)

    def tearDown(self):
        pass

    def _checkApplication(self, application):
        assert application.sid == 'TestApplicationSid'
        assert application.friendlyName == 'TestApplication'
