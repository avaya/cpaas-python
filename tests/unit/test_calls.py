import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.answered_by import AnsweredBy
from zang.domain.enums.call_status import CallStatus
from zang.domain.enums.audio_direction import AudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.transcribe_quality import TranscribeQuality
from zang.domain.enums.recording_audio_direction import RecordingAudioDirection

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestCalls(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.callsConnector

    def test_view(self):
        TestUtil.start('CallsTest', 'viewCall')
        call = self.connector.viewCall('TestCallSid')
        self.checkCall(call)

    def test_list(self):
        TestUtil.start('CallsTest', 'listCalls')
        calls = self.connector.listCalls(
            to='+123456',
            from_='+654321',
            status=CallStatus.COMPLETED,
            page=0,
            pageSize=10
        )
        assert len(calls.elements) == 1
        self.checkCall(calls.elements[0])

    def test_make_call(self):
        TestUtil.start('CallsTest', 'makeCall')
        call = self.connector.makeCall(
            to='+123456',
            from_='+654321',
            url='TestUrl',
            method=HttpMethod.GET,
            fallbackUrl='FallbackUrl',
            fallbackMethod=HttpMethod.POST,
            statusCallback='StatusCallback',
            statusCallbackMethod=HttpMethod.GET,
            heartbeatUrl='HeartbeatUrl',
            heartbeatMethod=HttpMethod.GET,
            forwardedFrom='1234',
            playDtmf='123#',
            timeout=122,
            hideCallerId=True,
            record=True,
            recordCallback='RecordCallback',
            recordCallbackMethod=HttpMethod.GET,
            transcribe=True,
            transcribeCallback='TranscribeCallback',
            straightToVoicemail=True,
            ifMachine='redirect',
            ifMachineUrl='IfMachineUrl',
            ifMachineMethod=HttpMethod.GET,
            sipAuthUsername='username',
            sipAuthPassword='password')
        self.checkCall(call)

    def test_interrupt_live_call(self):
        TestUtil.start('CallsTest', 'interruptLiveCall')
        call = self.connector.interruptLiveCall(
            'TestCallSid', 'TestUrl', HttpMethod.GET, 'canceled')
        self.checkCall(call)

    def test_send_digits_to_live_call(self):
        TestUtil.start('CallsTest', 'sendDigitsToLiveCall')
        call = self.connector.sendDigitsToLiveCall(
            'TestCallSid', '0123#', AudioDirection.OUT)
        self.checkCall(call)

    def test_recordLiveCall(self):
        TestUtil.start('CallsTest', 'recordLiveCall')
        call = self.connector.recordLiveCall(
            'TestCallSid',
            True,
            RecordingAudioDirection.BOTH,
            15,
            'TestUrl',
            RecordingFileFormat.MP3,
            True,
            True,
            TranscribeQuality.HYBRID,
            'TestTranscribeUrl')
        self.checkCall(call)

    def test_playAudioToLiveCall(self):
        TestUtil.start('CallsTest', 'playAudioToLiveCall')
        call = self.connector.playAudioToLiveCall(
            'TestCallSid', 'AudioUrl', RecordingAudioDirection.BOTH, True)
        self.checkCall(call)

    def test_applyVoiceEffect(self):
        TestUtil.start('CallsTest', 'applyVoiceEffect')
        call = self.connector.applyVoiceEffect(
            'TestCallSid', AudioDirection.OUT, 5, 4, 3, 2, 1)
        self.checkCall(call)

    def checkCall(self, call):
        assert call.answeredBy == AnsweredBy.TBD
        assert call.price == 0.1872
        assert call.callStatus == CallStatus.COMPLETED
