# -*- coding: utf-8 -*-

"""
zang.connectors.conferences_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Conferences` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.conference import Conference
from zang.domain.list.conferences import Conferences

from zang.domain.list.participants import Participants
from zang.domain.participant import Participant


class ConferencesConnector(BaseConnector):
    """
    Used for all forms of communication with the `Conferences`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(ConferencesConnector, self).__init__(executor)

    def viewConference(self, conferenceSid):
        """
        Shows information about a conference

        :param conferenceSid: SID of the conference for which you want to
            retrieve information
        :type conferenceSid: str

        :return: Information about the Conference
        :rtype: zang.domain.conference.Conference
        :raises ZangException:
        """
        conference = self._executor.read(
            ('Conferences', conferenceSid), Conference)
        return conference

    def listConferences(
            self,
            friendlyName=None,
            status=None,
            dateCreatedGte=None,
            dateCreatedLt=None,
            dateUpdatedGte=None,
            dateUpdatedLt=None,
            page=None,
            pageSize=None,):
        """
        List conferences associated with an account

        :param friendlyName: (optional) Filters conferences by the given
            FriendlyName.
        :param status: (optional) Filters conferences by the given status.
            Allowed values are "init", "in-progress", or "completed".
        :param dateCreatedGte: (optional) Filter by date created greater or
            equal then
        :param dateCreatedLt: (optional) Filter by date created less than
        :param dateUpdatedGte: (optional) Filter by date updated greater or
            equal then
        :param dateUpdatedLt: (optional) Filter by date updated less than
        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type friendlyName: str
        :type status: zang.domain.enums.conference_status.ConferenceStatus
        :type dateCreatedGte: datetime.date
        :type dateCreatedLt: datetime.date
        :type dateUpdatedGte: datetime.date
        :type dateUpdatedLt: datetime.date
        :type page: int
        :type pageSize: int

        :return: List of Conferences
        :rtype: zang.domain.list.conferences.Conferences
        :raises ZangException:
        """
        queryParams = {
            'FriendlyName': friendlyName,
            'Status': status,
            'DateCreated>': dateCreatedGte,
            'DateCreated<': dateCreatedLt,
            'DateUpdated>': dateUpdatedGte,
            'DateUpdated<': dateUpdatedLt,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        conferences = self._executor.read(
            ('Conferences',), Conferences, params)
        return conferences

    def viewParticipant(self, conferenceSid, participantSid):
        """
        Shows information about a Conference participant

        :param conferenceSid: SID of the conference for which you want to
            retrieve information
        :param participantSid: SID of the participant

        :type conferenceSid: str
        :type participantSid: str

        :return: Information about the Participant
        :rtype: zang.domain.participant.Participant
        :raises ZangException:
        """
        participant = self._executor.read(
            ('Conferences', conferenceSid, 'Participants', participantSid),
            Participant)
        return participant

    def listParticipants(
            self,
            conferenceSid,
            muted=None,
            deaf=None,
            page=None,
            pageSize=None,):
        """
        List participants in a conference.

        :param ConferenceSid: Conference SID.
        :param Muted: (optional) Filter by participants that are muted.
            Allowed values are "true" or "false".
        :param Deaf: (optional) Filter by participants that are deaf.
            Allowed values are "true" or "false".
        :param Page: (optional) Used to return a particular page within
            the list.
        :param PageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type ConferenceSid: str
        :type Muted: bool
        :type Deaf: bool
        :type Page: int
        :type PageSize: int

        :return: List of participants
        :rtype: zang.domain.list.participants.Participants
        :raises ZangException:
        """
        queryParams = {
            'Muted': muted,
            'Deaf': deaf,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        participants = self._executor.read(
            ('Conferences', conferenceSid, 'Participants',), Participants,
            params)
        return participants

    def deafOrMuteParticipant(
            self,
            conferenceSid,
            participantSid,
            muted=None,
            deaf=None,):
        """
        Set status of participant in a conference to muted or deaf

        :param conferenceSid: Conference SID
        :param participantSid: SID of the participant
        :param muted: (optional) Filter only muted participants
        :param deaf: (optional) Filter only deaf participants

        :type conferenceSid: str
        :type participantSid: str
        :type muted: (optional) bool
        :type deaf: (optional) bool

        :return: The participant in question.
        :rtype: zang.domain.participant.Participant
        :raises ZangException:
        """
        bodyParams = {
            'Muted': muted,
            'Deaf': deaf,
        }
        data = flatDict(bodyParams)
        participant = self._executor.update(
            ('Conferences', conferenceSid, 'Participants', participantSid),
            Participant, data=data)
        return participant

    def playAudioToParticipant(
            self,
            conferenceSid,
            participantSid,
            audioUrl=None,):
        """
        Plays an audio file to a conference participant

        :param conferenceSid: Conference SID
        :param participantSid: SID of the participant
        :param audioUrl: (optional) url A URL to the audio file that will be
            played to the participant.

        :type conferenceSid: str
        :type participantSid: str
        :type audioUrl: (optional) str

        :return: The participant in question.
        :rtype: zang.domain.participant.Participant
        :raises ZangException:
        """
        bodyParams = {
            'AudioUrl': audioUrl,
        }
        data = flatDict(bodyParams)
        participant = self._executor.update(
            ('Conferences', conferenceSid, 'Participants', participantSid,
             'Play'), Participant, data=data)
        return participant

    def hangupParticipant(self, conferenceSid, participantSid):
        """
        Hangs up a conference participant.

        :param conferenceSid: Conference SID
        :param participantSid: SID of the participant

        :type conferenceSid: str
        :type participantSid: str

        :return: The participant in question.
        :rtype: zang.domain.participant.Participant
        :raises ZangException:
        """
        participant = self._executor.delete(
            ('Conferences', conferenceSid, 'Participants', participantSid,),
            Participant)
        return participant
