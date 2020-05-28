# -*- coding: utf-8 -*-

"""
zang.connectors.recordings_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Recordings` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.recording import Recording
from zang.domain.list.recordings import Recordings


class RecordingsConnector(BaseConnector):
    """
    Used for all forms of communication with the `Recordings`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewRecording(self, recordingSid):
        """
        Shows information on some recording

        :param recordingSid: Recording SID.
        :type recordingSid: str

        :return: `Recording` object
        :rtype: zang.domain.recording.Recording
        :raises ZangException:
        """
        recording = self._executor.read(
            ('Recordings', recordingSid), Recording)
        return recording

    def listRecordings(
            self,
            callSid=None,
            dateCreatedGte=None,
            dateCreatedLt=None,
            page=None,
            pageSize=None,):
        """
        Shows info on all recordings associated with some account

        :param callSid: Filters by recordings associated with a given CallSid.
        :type dateCreatedGte: (optional) Filter by date created greater or
            equal then
        :type dateCreatedLt: (optional) Filter by date created less than
        :param page: Used to return a particular page within the list.
        :param pageSize: Used to specify the amount of list items to return
            per page.

        :type callSid: str
        :type dateCreatedGte: datetime.date
        :type dateCreatedLt: datetime.date
        :type page: int
        :type pageSize: int

        :return: `Recordings` object
        :rtype: zang.domain.list.recordings.Recordings
        :raises ZangException:
        """
        queryParams = {
            'CallSid': callSid,
            'DateCreated>': dateCreatedGte,
            'DateCreated<': dateCreatedLt,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        recordings = self._executor.read(('Recordings',), Recordings, params)
        return recordings

    def recordCall(
            self,
            callSid,
            record,
            direction=None,
            timeLimit=None,
            callbackUrl=None,
            fileFormat=None,
            trimSilence=None,
            transcribe=None,
            transcribeQuality=None,
            transcribeCallback=None,):
        """
        Records a Zang call

        :param callSid: Call SID.
        :param record: Specifies if a call recording should start or end.
            Allowed values are "true" to start recording and "false" to end
            recording. Any number of simultaneous, separate recordings can
            be initiated.
        :param direction: Specifies which audio stream to record. Allowed
            alues are "in" to record the incoming caller's audio, "out" to
            record the outgoing caller's audio, and "both" to record both.
        :param timeLimit: The maximum duration of the recording. Allowed value
            is an integer greater than 0.
        :param callbackUrl: A URL that will be requested when the recording
            ends, sending information about the recording. The longer the
            recording, the longer the delay in processing the recording and
            requesting the CallbackUrl. Url length is limited to 200
            characters.
        :param fileFormat: Specifies the file format of the recording.
            Allowed values are "mp3" or "wav" - any other value will default
            to "mp3".
        :param trimSilence: Trims all silence from the beginning of the
            recording. Allowed values are "true" or "false" - any other value
            will default to "false".
        :param transcribe: Specifies if this recording should be transcribed.
            Allowed values are "true" and "false" - all other values will
            default to "false".
        :param transcribeQuality: Specifies the quality of the transcription.
            Allowed values are "auto" for automated transcriptions and
            "hybrid" for human-reviewed transcriptions - all other values will
            default to "auto".
        :param transcribeCallback: A URL that will be requested when the call
            ends, sending information about the transcription. The longer the
            recording, the longer the delay in processing the transcription
            and requesting the TranscribeCallback. URL length is limited to
            200 characters.

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
        :type transcribeQuality:zang.domain.enums.transcribe_quality.
            TranscribeQuality
        :type transcribeCallback: str

        :return: `Recording` object
        :rtype: zang.domain.recording.Recording
        :raises ZangException:
        """
        bodyParams = {
            'Record': record,
            'Direction': direction,
            'TimeLimit': timeLimit,
            'CallbackUrl': callbackUrl,
            'FileFormat': fileFormat,
            'TrimSilence': trimSilence,
            'Transcribe': transcribe,
            'TranscribeQuality': transcribeQuality,
            'TranscribeCallback': transcribeCallback,
        }
        data = flatDict(bodyParams)
        recording = self._executor.create(
            ('Calls', callSid, 'Recordings', ), Recording, data)
        return recording

    def deleteRecording(self, recordingSid):
        """
        Deletes a recording

        :param recordingSid: Recording SID.
        :type recordingSid: str

        :return: `Recording` object
        :rtype: zang.domain.recording.Recording
        :raises ZangException:
        """
        recording = self._executor.delete(
            ('Recordings', recordingSid), Recording)
        return recording
