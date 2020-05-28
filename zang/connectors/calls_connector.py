# -*- coding: utf-8 -*-

"""
zang.connectors.calls_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Calls` endpoint
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.call import Call
from zang.domain.list.calls import Calls


class CallsConnector(BaseConnector):
    """
    Used for all forms of communication with the `Calls`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(CallsConnector, self).__init__(executor)

    def viewCall(self, callSid):
        """
        View all information about a call.

        :param callSid:
        :type callSid: str

        :return: An `Call` resource.
        :rtype: zang.domain.call.Call
        :raises: ZangException
        """
        call = self._executor.read(('Calls', callSid), Call)
        return call

    def listCalls(
            self,
            to=None,
            from_=None,
            status=None,
            startTimeGte=None,
            startTimeLt=None,
            page=None,
            pageSize=None,):
        """
        List all calls associated with your account or filter results.filter.

        :param to: Filter by a specific number calls were made to.
        :param from: Filter by a specific number calls were made from.
        :param status: Filter by calls with the specified status. Allowed
            values are "ringing", "in-progress", "queued", "busy",
            "completed", "no-answer", and "failed".
        :param startTimeGte: Filter by start time greater or equal than
        :param startTimeLt: Filter by start time less than

        :param page: Used to return a particular page within the list.
        :param pageSize: Used to specify the amount of list items to return
            per page.

        :type to: str
        :type from: str
        :type status: zang.domain.enums.call_status.CallStatus
        :type startTimeGt: datetime.date
        :type startTimeLt: datetime.date
        :type page: int
        :type pageSize: int

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        queryParams = {
            'To': to,
            'From': from_,
            'Status': status,
            'StartTime>': startTimeGte,
            'StartTime<': startTimeLt,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        calls = self._executor.read(('Calls',), Calls, params)
        return calls

    def makeCall(
            self,
            to,
            from_,
            url,
            method=None,
            fallbackUrl=None,
            fallbackMethod=None,
            statusCallback=None,
            statusCallbackMethod=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            forwardedFrom=None,
            playDtmf=None,
            timeout=None,
            hideCallerId=None,
            record=None,
            recordCallback=None,
            recordCallbackMethod=None,
            transcribe=None,
            transcribeCallback=None,
            straightToVoicemail=None,
            ifMachine=None,
            ifMachineUrl=None,
            ifMachineMethod=None,
            sipAuthUsername=None,
            sipAuthPassword=None,):
        """
        :param to: The phone number or SIP endpoint to call. Phone number
            should be in international format and one recipient per request.
            For e.g, to dial a number in the US, the To should be,
            +17325551212. SIP endpoints must be prefixed with sip:
            e.g sip:12345@sip.zang.io.
        :param from: The number to display as calling (i.e. Caller ID).
            The value does not have to be a real phone number or even in a
            validformat. For example, 8143 could be passed to the From
            parameter and would be displayed as the caller ID. Spoofed
            calls carry an additional charge.
        :param url: The URL requested once the call connects. This URL mustbe
            valid and should return InboundXML containing instructions on how
            to process your call. A badly formatted URL will NOT fallback to
            the FallbackUrl but return an error without placing the call. URL
            length is limited to 200 characters.
        :param method: (optional) The HTTP method used to request the URL
            once the call connects. Valid parameters are GET and POST - any
            other value will default to POST.
        :param fallbackUrl:  (optional)URL used if the required URL is
            unavailable or if any errors occur during execution of the
            InboundXML returned by the required URL. Url length is limited
            to 200 characters.
        :param fallbackMethod:  (optional)The HTTP method used to request
            the FallbackUrl once the call connects. Valid parameters are GET
            and POST - any other value will default to POST.
        :param statusCallback:  (optional)A URL that will be requested when
            the call connects and ends, sending information about the call.
            URL length is limited to 200 characters.
        :param statusCallbackMethod:  (optional)The HTTP method used to
            request the StatusCallback URL. Valid parameters are GET and
            POST - any other value will default to POST.
        :param heartbeatUrl:  (optional)A URL that will be requested every
            60 seconds during the call, sending information about the call.
            The HeartbeatUrl will NOT be requested unless at least 60 seconds
            of call time have elapsed. URL length is limited to 200 characters.
        :param heartbeatMethod:  (optional)The HTTP method used to request
            the HeartbeatUrl. Valid parameters are GET and POST - any other
            value will default to POST.
        :param forwardedFrom:  (optional)Specifies the Forwarding From number
            to pass to the carrier.
        :param playDtmf:  (optional)Dial digits or play tones using DTMF as
            soon as the call connects. Useful for navigating IVRs. Allowed
            values for digits are 0-9, #, *, W, or w (W and w are for .5
            second pauses), for example 142##* (spaces are valid). Tones
            follow the @1000 syntax, for example to play the tone 4 for two
            seconds, 4@2000 (milliseconds) would be used.
        :param timeout:  (optional)Number of seconds call stays on line while
            waiting for an answer. The max time limit is 999.
        :param hideCallerId:  (optional)Specifies if the Caller ID will be
            blocked. Allowed positive values are "true" and "True" - any
            other value will default to "false".
        :param record:  (optional)Specifies if this call should be recorded.
            Allowed positive values are "true", "True" and "1" - any other
            value will default to "false". Please note that no more than 5
            recordings may be associated with a single call.
        :param recordCallback:  (optional)The URL some parameters regarding
            the recording will be passed to once it is completed. The longer
            the recording time, the longer the process delay in returning
            the recording information. If no RecordCallback is given, the
            recording will still be saved to the system and available
            either in your Recording Logs or via a REST List Recordings
            request. Url length is limited to 200 characters.
        :param recordCallbackMethod:  (optional)The HTTP method used to
            request the RecordCallback. Valid parameters are GET and POST
            - any other value will default to POST.
        :param transcribe:  (optional)Specifies whether this call should be
            transcribed. Allowed positive values are "true", "True", and "1".
        :param transcribeCallback:  (optional)The URL some parameters
            regarding the transcription will be passed to once it is
            completed. The longer the recording time, the longer the process
            delay in returning the transcription information. If no
            TranscribeCallback is given, the recording will still be saved to
            the system and available either in your Transcriptions Logs or
            via a REST List Transcriptions (ADD URL LINK) request. Url length
            is limited to 200 characters.
        :param straightToVoicemail:  (optional)Specifies whether this call
            should be sent straight to the user's voicemail. Allowed positive
            values are "true" and "True" - any other value will default to
            "false".
        :param ifMachine:  (optional)Specifies how Zang should handle this
            call if it goes to voicemail. Allowed values are "continue" to
            proceed as normal, "redirect" to redirect the call to the
            ifMachineUrl, or "hangup" to hang up the call. Hangup occurs when
            the tone is played. IfMachine accuracy is around 90% and may not
            work in all countries.
        :param ifMachineUrl:  (optional)The URL Zang will redirect to for
            instructions if a voicemail machine is detected while the
            IfMachine parameter is set to "redirect". Url length is
            limited to 200 characters.
        :param ifMachineMethod:  (optional)The HTTP method used to request
            the IfMachineUrl. Valid parameters are GET and POST - any other
            value will default to POST.
        :param sipAuthUsername:  (optional)Your authenticated SIP username,
            used only for SIP calls.
        :param sipAuthPassword:  (optional)Your authenticated SIP password,
            used only for SIP calls.

        :type to: str
        :type from_: str
        :type url: str
        :type method: zang.domain.enums.http_method.HttpMethod
        :type fallbackUrl: str
        :type fallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type statusCallback: str
        :type statusCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type heartbeatUrl: str
        :type heartbeatMethod: zang.domain.enums.http_method.HttpMethod
        :type forwardedFrom: str
        :type playDtmf: str
        :type timeout: int
        :type hideCallerId:
        :type record: bool
        :type recordCallback: str
        :type recordCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type transcribe: bool
        :type transcribeCallback: str
        :type straightToVoicemail: bool
        :type ifMachine: zang.domain.enums.if_machine.IfMachine
        :type ifMachineUrl: str
        :type ifMachineMethod: zang.domain.enums.http_method.HttpMethod
        :type sipAuthUsername: str
        :type sipAuthPassword: str

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {
            'To': to,
            'From': from_,
            'Url': url,
            'Method': method,
            'FallbackUrl': fallbackUrl,
            'FallbackMethod': fallbackMethod,
            'StatusCallback': statusCallback,
            'StatusCallbackMethod': statusCallbackMethod,
            'HeartbeatUrl': heartbeatUrl,
            'HeartbeatMethod': heartbeatMethod,
            'ForwardedFrom': forwardedFrom,
            'PlayDtmf': playDtmf,
            'Timeout': timeout,
            'HideCallerId': hideCallerId,
            'Record': record,
            'RecordCallback': recordCallback,
            'RecordCallbackMethod': recordCallbackMethod,
            'Transcribe': transcribe,
            'TranscribeCallback': transcribeCallback,
            'StraightToVoicemail': straightToVoicemail,
            'IfMachine': ifMachine,
            'IfMachineUrl': ifMachineUrl,
            'IfMachineMethod': ifMachineMethod,
            'SipAuthUsername': sipAuthUsername,
            'SipAuthPassword': sipAuthPassword,
        }
        data = flatDict(bodyParams)
        call = self._executor.create(('Calls',), Call, data=data)
        return call

    def interruptLiveCall(
            self,
            callSid,
            url=None,
            method=None,
            status=None,):
        """
        Send new instructions to the call.

        :param callSid: Call SID.
        :param url: The URL that in-progress calls will request for
            new instructions.
        :param method: The HTTP method used to request the redirect URL.
            Valid parameters are GET and POST.
        :param status: The status used to end the call. Allowed values are
            "canceled" for ending queued or ringing calls, and "completed"
            to end in-progress calls in addition to queued and ringing calls.

        :type callSid: str
        :type url: str
        :type method: zang.domain.enums.http_method.HttpMethod
        :type status: zang.domain.enums.end_call_status.EndCallStatus

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {'Url': url, 'Method': method, 'Status': status}
        data = flatDict(bodyParams)
        call = self._executor.update(('Calls', callSid), Call, data=data)
        return call

    def sendDigitsToLiveCall(
            self,
            callSid,
            playDtmf=None,
            playDtmfDirection=None,):
        """
        Use DTMF tones to mimic button presses.

        :param callSid: Call SID.
        :param playDtmf: Allowed values are the digits 0-9, #, *, W, or w.
            "w" and "W"stand for 1/2 second pauses. You can combine these
            values together, for example, "12ww34". Tones are also supported
            and follow the @1000 syntax, for example to play the tone 4 for
            two seconds, 4@2000 (milliseconds) would be used.
        :param playDtmfDirection: Specifies which leg of the call DTMF tones
            will be played on. Allowed values are “in” to send tones to the
            incoming caller or “out” to send tones to the out going caller.

        :type callSid: str
        :type playDtmf: str
        :type playDtmfDirection: zang.domain.enums.audio_direction.
            AudioDirection

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {
            'PlayDtmf': playDtmf,
            'PlayDtmfDirection': playDtmfDirection
        }
        data = flatDict(bodyParams)
        call = self._executor.update(('Calls', callSid), Call, data=data)
        return call

    def recordLiveCall(
            self,
            callSid,
            record,
            direction=None,
            timeLimit=None,
            callbackUrl=None,
            fileFormat=None,
            trimSilence=None,
            transcribe=None,
            transcriptionQuality=None,
            transcribeCallback=None,):
        """
        Options include time limit, file format, trimming silence and
        transcribing

        :param callSid: Call SID.
        :param record: Specifies if a call recording should start or end.
            Allowed values are "true" to start recording and "false" to end
            recording. Any number of simultaneous, separate recordings can
            be initiated.
        :param direction:  Specifies which audio stream to record. Allowed
            values are "in" to record the incoming caller's audio, "out" to
            record the outgoing caller's audio, and "both" to record both.
        :param timeLimit:  The maximum duration of the recording. Allowed
            value is an integer greater than 0.
        :param callbackUrl:    A URL that will be requested when the
            recording ends, sending information about the recording. The
            longer the recording, the longer the delay in processing the
            recording and requesting the CallbackUrl. Url length is limited
            to 200 characters.
        :param fileFormat: Specifies the file format of the recording.
            Allowed values are "mp3" or "wav" - any other value will default
            to "mp3".
        :param trimSilence:    Trims all silence from the beginning of the
            recording. Allowed values are "true" or "false" - any other value
            will default to "false".
        :param transcribe: Specifies if this recording should be transcribed.
            Allowed values are "true" and "false" - all other values will
            default to "false".
        :param transcribeQuality:  Specifies the quality of the transcription.
            Allowed values are "auto" for automated transcriptions and
            "hybrid" for human-reviewed transcriptions - all other values will
            default to "auto".
        :param transcribeCallback: A URL that will be requested when the call
            ends, sending information about the transcription. The longer
            the recording, the longer the delay in processing the
            transcription and requesting the TranscribeCallback. Url length
            is limited to 200 characters.

        :type callSid: str
        :type record: bool
        :type direction: zang.domain.enums.recording_audio_direction.
            RecordingAudioDirection
        :type timeLimit: int
        :type callbackUrl: str
        :type fileFormat: zang.domain.enums.recording_file_format.
            RecordingFileFormat
        :type trimSilence: bool
        :type transcribe: bool
        :type transcribeQuality: zang.domain.enums.transcribe_quality.
            TranscribeQuality
        :type transcribeCallback: str

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {
            'Record': record,
            'Direction': direction,
            'TimeLimit': timeLimit,
            'CallbackUrl': callbackUrl,
            'FileFormat': fileFormat,
            'TrimSilence': trimSilence,
            'Transcribe': transcribe,
            'TranscribeQuality': transcriptionQuality,
            'TranscribeCallback': transcribeCallback,
        }
        data = flatDict(bodyParams)
        call = self._executor.update(
            ('Calls', callSid, 'Recordings'), Call, data=data)
        return call

    def playAudioToLiveCall(
            self,
            callSid,
            audioUrl,
            direction=None,
            loop=None,):
        """
        Options include restricting to one caller and looping.

        :param callSid: Call SID.
        :param audioUrl: A URL returning the sound file to play.
            Progressive downloads and SHOUTCAST streaming are also supported.
        :param direction: Specifies which caller will hear the played audio.
            Allowed values are "in" to play audio to the incoming caller,
            "out" to play to the outgoing caller, and "both" to play the
            audio to both callers.
        :param loop: Specifies whether the audio will loop. Allowed values
            are "true" and "false".

        :type callSid: str
        :type audioUrl: str
        :type direction: zang.domain.enums.recording_audio_direction.
            RecordingAudioDirection
        :type loop: bool

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {
            'AudioUrl': audioUrl,
            'Direction': direction,
            'Loop': loop,
        }
        data = flatDict(bodyParams)
        call = self._executor.update(
            ('Calls', callSid, 'Play'), Call, data=data)
        return call

    def applyVoiceEffect(
            self,
            callSid,
            direction,
            pitch=None,
            pitchSemiTones=None,
            pitchOctaves=None,
            rate=None,
            tempo=None,):
        """
        Applies voice effect on the call.

        :param CallSid: Call SID.
        :param AudioDirection: Specifies which caller should have their voice
            modified. Allowed values are "in" for the incoming caller and
            "out" for the outgoing caller. This value can be changed as
            often as you like to control live call flow.
        :param Pitch: Sets the pitch. The lower the value, the lower the
            tone. Allowed values are integers greater than 0.
        :param PitchSemiTones: Changes the pitch of audio in semitone
            intervals. Allowed values are integers between -14 and 14.
        :param PitchOctaves: Changes the pitch of the audio in octave
            intervals. Allowed values are integers between -1 and 1.
        :param Rate: Sets the rate. The lower the value, the lower the
            rate. Allowed values are integers greater than 0.
        :param Tempo: Sets the tempo. The lower the value, the slower the
            tempo. Allowed values are integers greater than 0.

        :type CallSid: str
        :type AudioDirection: zang.domain.enums.audio_direction.AudioDirection
        :type Pitch: int
        :type PitchSemiTones: int
        :type PitchOctaves: int
        :type Rate: int
        :type Tempo: int

        :return: An `Calls` resource.
        :rtype: zang.domain.list.calls.Calls
        :raises: ZangException
        """
        bodyParams = {
            'AudioDirection': direction,
            'Pitch': pitch,
            'PitchSemiTones': pitchSemiTones,
            'PitchOctaves': pitchOctaves,
            'Rate': rate,
            'Tempo': tempo,
        }
        data = flatDict(bodyParams)
        call = self._executor.update(
            ('Calls', callSid, 'Effect'), Call, data=data)
        return call
