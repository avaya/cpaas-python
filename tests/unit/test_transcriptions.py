import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.transcribe_quality import TranscribeQuality
from zang.domain.enums.transcription_status import TranscriptionStatus

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL
from datetime import date


class TestTranscriptions(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.transcriptionsConnector

    def test_view(self):
        TestUtil.start('TranscriptionsTest', 'viewTranscription')
        obj = self.connector.viewTranscription('TestTranscriptionSid')
        self.checkTranscription(obj)

    def test_list(self):
        TestUtil.start('TranscriptionsTest', 'listTranscriptions')
        obj = self.connector.listTranscriptions(
            status=TranscriptionStatus.COMPLETED,
            dateTranscribedGte=date(2016, 12, 12),
            dateTranscribedLt=date(2017, 3, 19),
            page=0,
            pageSize=33)
        assert len(obj.elements) == 2
        assert (obj.elements[0].transcriptionText ==
                'Hello from St. Cloud. We hope you like.')

    def test_transcribeRecording(self):
        TestUtil.start('TranscriptionsTest', 'transcribeRecording')
        obj = self.connector.transcribeRecording(
            'TestRecordingSid', 'TranscribeCallback', HttpMethod.GET, 0, 33,
            TranscribeQuality.HYBRID)
        self.checkTranscription(obj)

    def test_transcribeAudioUrl(self):
        TestUtil.start('TranscriptionsTest', 'transcribeAudioUrl')
        obj = self.connector.transcribeAudioUrl(
            audioUrl='AudioUrl',
            transcribeCallback='TranscribeCallback',
            sliceStart=0,
            sliceDuration=33,
            callbackMethod=HttpMethod.GET,
            quality=TranscribeQuality.AUTO)
        self.checkTranscription(obj)

    def checkTranscription(self, transcription):
        assert ('Hello from St. Cloud. We hope you like this.' ==
                transcription.transcriptionText)
