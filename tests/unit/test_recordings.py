import unittest
from datetime import date

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.transcribe_quality import TranscribeQuality
from zang.domain.enums.recording_audio_direction import RecordingAudioDirection

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestRecordings(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.recordingsConnector

    def test_view_recodring(self):
        TestUtil.start('RecordingsTest', 'viewRecording')
        recording = self.connector.viewRecording('TestRecordingSid')
        self.checkRecording(recording)

    def test_list_recodring(self):
        TestUtil.start('RecordingsTest', 'listRecordings')
        recordings = self.connector.listRecordings(
            'TestCallSid', dateCreatedGte=date(2016, 12, 12),
            dateCreatedLt=date(2017, 3, 19), page=0, pageSize=33)
        recording = recordings.elements[0]
        assert recording.price == 0.00
        assert recording.duration == 15

    def test_record_call(self):
        TestUtil.start('RecordingsTest', 'recordCall')
        recording = self.connector.recordCall(
            callSid='TestCallSid',
            record=True,
            direction=RecordingAudioDirection.OUT,
            timeLimit=1337,
            callbackUrl='CallbackUrl',
            fileFormat=RecordingFileFormat.WAV,
            trimSilence=True,
            transcribe=True,
            transcribeQuality=TranscribeQuality.HYBRID,
            transcribeCallback='TranscribeCallback')
        self.checkRecording(recording)

    def test_delete_recodring(self):
        TestUtil.start('RecordingsTest', 'deleteRecording')
        recording = self.connector.deleteRecording('TestRecordingSid')
        self.checkRecording(recording)

    def checkRecording(self, recording):
        assert (
            recording.recordingUrl ==
            ('http://recordings.telapi.com/' +
                'RBfcc94a3e2b5d4e4c89f7017d6387ffb8' +
                '/RE4288908463cd614b41084509ad8893a7.mp3'))
