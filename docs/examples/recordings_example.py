from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.recording_audio_direction import RecordingAudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.transcribe_quality import TranscribeQuality


from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
recordingsConnector = ConnectorFactory(configuration).recordingsConnector


# view recording
try:
    recording = recordingsConnector.viewRecording('TestRecordingSid')
    print(recording.duration)
except ZangException as ze:
    print(ze)


# list recordings
try:
    recording = recordingsConnector.listRecordings('TestCallSid')
    print(recording.total)
except ZangException as ze:
    print(ze)


# record call
try:
    recording = recordingsConnector.recordCall(
        callSid='TestCallSid',
        record=True,
        direction=RecordingAudioDirection.OUT,
        timeLimit=1337,
        callbackUrl='CallbackUrl',
        fileFormat=RecordingFileFormat.WAV,
        trimSilence=True,
        transcribe=True,
        transcriptionQuality=TranscribeQuality.HYBRID,
        transcribeCallback='TranscribeCallback'),
    print(recording.total)
except ZangException as ze:
    print(ze)


# delete recording
try:
    recording = recordingsConnector.deleteRecording('TestRecordingSid')
    print(recording.price)
except ZangException as ze:
    print(ze)
