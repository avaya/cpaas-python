# -*- coding: utf-8 -*-

"""
zang.connectors.transcriptions_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Transcriptions` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.transcription import Transcription
from zang.domain.list.transcriptions import Transcriptions


class TranscriptionsConnector(BaseConnector):
    """
    Used for all forms of communication with the `Transcriptions`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewTranscription(self, transcriptionSid):
        """
        Shows information on some recording

        :param recordingSid: Transcription SID.
        :type recordingSid: str

        :return: `Transcription` object
        :rtype: zang.domain.transcription.Transcription
        :raises ZangException:
        """
        transcription = self._executor.read(
            ('Transcriptions', transcriptionSid), Transcription)
        return transcription

    def listTranscriptions(
            self,
            status=None,
            dateTranscribedGte=None,
            dateTranscribedLt=None,
            page=None,
            pageSize=None,):
        """
        :param status: Filter by transcriptions with a given status. Allowed
            values are "completed", "in-progress", and "failed".
        :param dateTranscribedGte: Filter by date transcribed greater or
            equal than
        :param dateTranscribedLt: filter by date transcribed less than
        :param page: Used to return a particular page within the list.
        :param pageSize: Used to specify the amount of list items to return
            per page.

        :type status: zang.domain.enums.transcription_status.
            TranscriptionStatus
        :param dateTranscribedGte: datetime.date
        :param dateTranscribedLt: datetime.date
        :type page: int
        :type pageSize: int

        :return: `Transcriptions` object
        :rtype: zang.domain.list.transcriptions.Transcriptions
        :raises ZangException:
        """
        queryParams = {
            'Status': status,
            'DateTranscribed>': dateTranscribedGte,
            'DateTranscribed<': dateTranscribedLt,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        transcriptions = self._executor.read(
            ('Transcriptions',), Transcriptions, params)
        return transcriptions

    def transcribeRecording(
            self,
            recordingSid,
            transcribeCallback=None,
            callbackMethod=None,
            sliceStart=None,
            sliceDuration=None,
            quality=None,):
        """
        Transcribes some recording

        :param recordingSid: Recording SID.
        :param transcribeCallback: (option) The URL some parameters regarding
            the transcription will be passed to once it is completed. The
            longer the recording time, the longer the process delay in
            returning the transcription information. If no TranscribeCallback
            is given, the recording will still be saved to the system and
            available either in your Transcriptions Logs or via a REST List
            Transcriptions (ADD URL LINK) request. URL length is limited to
            200 characters.
        :param callbackMethod: The (option) HTTP method used to request the
            TranscribeCallback. Valid parameters are GET and POST - any other
            value will default to POST.
        :param sliceStart: Start (option) point for slice transcription
            (in seconds).
        :param sliceDuration: Duration (option) of slice transcription
            (in seconds).
        :param quality: Specifies (option) the transcription quality.
            Transcription price differs for each quality tier. See pricing
            page for details. Allowed values are "auto", "hybrid" and
            "keywords", where "auto" is a machine-generated transcription,
            "hybrid" is reviewed by a human for accuracy and "keywords"
            returns topics and keywords for given audio file.

        :type recordingSid: str
        :type transcribeCallback: str
        :type callbackMethod: zang.domain.enums.http_method.HttpMethod
        :type sliceStart: int
        :type sliceDuration: int
        :type quality: zang.domain.enums.transcribe_quality.TranscribeQuality

        :return: `Transcriptions` object
        :rtype: zang.domain.list.transcriptions.Transcriptions
        :raises ZangException:
        """
        queryParams = {
            'TranscribeCallback': transcribeCallback,
            'CallbackMethod': callbackMethod,
            'SliceStart': sliceStart,
            'SliceDuration': sliceDuration,
            'Quality': quality,
        }
        params = flatDict(queryParams)
        transcription = self._executor.update(
            ('Recordings', recordingSid, 'Transcriptions'), Transcription,
            params)
        return transcription

    def transcribeAudioUrl(
            self,
            audioUrl=None,
            transcribeCallback=None,
            sliceStart=None,
            sliceDuration=None,
            callbackMethod=None,
            quality=None,):
        """
        Transcribes an audio file on some URL

        :param audioUrl: (option) URL where the audio to be transcribed
            is located.
        :param transcribeCallback: (option) URL that will be requested when
            the transcription has finished processing.
        :param sliceStart: (option) Start point for slice transcription
            (in seconds).
        :param sliceDuration: (option) Duration of slice transcription
            (in seconds).
        :param callbackMethod: (option) Specifies the HTTP method to use when
            requesting the TranscribeCallback URL. Allowed values are
            "POST" and "GET".
        :param quality: (option) Specifies the transcription quality.
            Transcription price differs for each quality tier. See pricing
            page for details. Allowed values are "auto", "hybrid" and
            "keywords", where "auto" is a machine-generated transcription,
            "hybrid" is reviewed by a human for accuracy and "keywords"
            returns topics and keywords for given audio file.

        :type audioUrl: str
        :type transcribeCallback: str
        :type sliceStart: int
        :type sliceDuration: int
        :type callbackMethod: zang.domain.enums.http_method.HttpMethod
        :type quality: zang.domain.enums.transcribe_quality.TranscribeQuality

        :return: `Transcriptions` object
        :rtype: zang.domain.list.transcriptions.Transcriptions
        :raises ZangException:
        """
        bodyParams = {
            'AudioUrl': audioUrl,
            'TranscribeCallback': transcribeCallback,
            'SliceStart': sliceStart,
            'SliceDuration': sliceDuration,
            'CallbackMethod': callbackMethod,
            'Quality': quality,
        }
        data = flatDict(bodyParams)
        transcription = self._executor.update(
            ('Transcriptions',), Transcription, data)
        return transcription
