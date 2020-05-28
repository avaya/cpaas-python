from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.transcription_status import TranscriptionStatus
from zang.domain.enums.transcribe_quality import TranscribeQuality
from zang.domain.enums.http_method import HttpMethod

from datetime import date
from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
transcriptionsConnector = ConnectorFactory(
    configuration).transcriptionsConnector


# view usage
try:
    transcription = transcriptionsConnector.viewTranscription(
        'TestTranscriptionSid')
    print(transcription.price)
except ZangException as ze:
    print(ze)


# list usages
try:

    transcriptions = transcriptionsConnector.listTranscriptions(
        status=TranscriptionStatus.COMPLETED,
        dateTranscribedGte=date(2016, 12, 31),
        dateTranscribedLt=date(2017, 12, 31),
        page=0,
        pageSize=33)
    print(transcriptions.total)
except ZangException as ze:
    print(ze)


# transcribe recording
try:
    transcription = transcriptionsConnector.transcribeRecording(
        "TestRecordingSid",
        transcribeCallback="TranscribeCallback",
        callbackMethod=HttpMethod.GET,
        sliceStart=0,
        sliceDuration=33,
        quality=TranscribeQuality.HYBRID)
    print(transcription.duration)
except ZangException as ze:
    print(ze)


# transcribe audio url
try:
    transcription = transcriptionsConnector.transcribeAudioUrl(
        audioUrl="AudioURl",
        transcribeCallback="TranscribeCallback",
        sliceStart=0,
        sliceDuration=33,
        callbackMethod=HttpMethod.GET,
        quality=TranscribeQuality.AUTO)
    print(transcription.duration)
except ZangException as ze:
    print(ze)
