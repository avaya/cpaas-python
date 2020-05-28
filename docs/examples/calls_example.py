from datetime import date
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.call_status import CallStatus
from zang.domain.enums.http_method import HttpMethod
from zang.domain.enums.if_machine import IfMachine
from zang.domain.enums.end_call_status import EndCallStatus
from zang.domain.enums.audio_direction import AudioDirection
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.domain.enums.recording_audio_direction import RecordingAudioDirection
from zang.domain.enums.transcribe_quality import TranscribeQuality


from zang.exceptions.zang_exception import ZangException

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
callsConnector = ConnectorFactory(configuration).callsConnector


# view call
try:
    call = callsConnector.viewCall('TestCallSid')
    print(call.duration)
except ZangException as ze:
    print(ze)


# list calls
try:
    startTimeGte = date(2017, 4, 1)
    calls = callsConnector.listCalls(
        to='+123456',
        from_='+654321',
        status=CallStatus.COMPLETED,
        startTimeGte=date(2016, 12, 31),
        startTimeLt=date(2017, 12, 31),
        page=0,
        pageSize=10)
    print(calls.total)
    if calls.e.elements:
        for call in calls.elements:
            print(call.duration)
except ZangException as ze:
    print(ze)


# make call
try:
    call = callsConnector.makeCall(
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
        ifMachine=IfMachine.REDIRECT,
        ifMachineUrl='IfMachineUrl',
        ifMachineMethod=HttpMethod.GET,
        sipAuthUsername='username',
        sipAuthPassword='password')
    print(call.sid)
except ZangException as ze:
    print(ze)


# interrupt live call
try:
    call = callsConnector.interruptLiveCall(
        'TestCallSid',
        url='TestUrl',
        method=HttpMethod.GET,
        status=EndCallStatus.CANCELED)
    print(call.status)
except ZangException as ze:
    print(ze)


# send digits to live call
try:
    call = callsConnector.sendDigitsToLiveCall(
        'TestCallSid',
        playDtmf='0123#',
        playDtmfDirection=AudioDirection.OUT)
    print(call.status)
except ZangException as ze:
    print(ze)


# record live call
try:
    call = callsConnector.recordLiveCall(
        'TestCallSid',
        True,
        direction=RecordingAudioDirection.BOTH,
        timeLimit=15,
        callbackUrl='TestUrl',
        fileFormat=RecordingFileFormat.MP3,
        trimSilence=True,
        transcribe=True,
        transcriptionQuality=TranscribeQuality.HYBRID,
        transcribeCallback='TestTranscribeUrl',)
    print(call.status)
except ZangException as ze:
    print(ze)


# play audio to live call
try:
    call = callsConnector.playAudioToLiveCall(
        'TestCallSid', 'AudioUrl', RecordingAudioDirection.BOTH, True)
    print(call.status)
except ZangException as ze:
    print(ze)


# apply voice effect
try:
    call = callsConnector.playAudioToLiveCall(
        'TestCallSid', AudioDirection.OUT, 5, 4, 3, 2, 1)
    print(call.status)
except ZangException as ze:
    print(ze)
