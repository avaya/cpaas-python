from datetime import date
from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.conference_status import ConferenceStatus

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
conferencesConnector = ConnectorFactory(configuration).conferencesConnector


# view conference
try:
    conference = conferencesConnector.viewConference('TestConferenceSid')
    print(conference.friendlyName)
except ZangException as ze:
    print(ze)


# list conferences
try:
    fromDate = date(2016, 12, 31)
    toDate = date(2017, 12, 31)
    conferences = conferencesConnector.listConferences(
        friendlyName='TestConferenceSid',
        status=ConferenceStatus.COMPLETED,
        dateCreatedGte=fromDate,
        dateCreatedLt=toDate,
        dateUpdatedGte=fromDate,
        dateUpdatedLt=toDate,
        page=0,
        pageSize=33)
    if conferences and conferences.elements:
        for conference in conferences.elements:
            print(conference.friendlyName)
except ZangException as ze:
    print(ze)


# view participant
try:
    conference = conferencesConnector.viewConference('TestConferenceSid')
    print(conference.friendlyName)
except ZangException as ze:
    print(ze)

# list participants
try:
    participants = conferencesConnector.listParticipants(
        'TestConferenceSid', False, False, 0, 33)
    print(participants.total)
except ZangException as ze:
    print(ze)

# mute/deaf participant
try:
    participant = conferencesConnector.deafOrMuteParticipant(
        'TestConferenceSid', 'TestParticipantSid', True, True)
    print(participant.muted)
except ZangException as ze:
    print(ze)

# play audio to participant
try:
    participant = conferencesConnector.playAudioToParticipant(
        'TestConferenceSid', 'TestParticipantSid',
        'http://mydomain.com/audio.mp3')
    print(participant.duration)
except ZangException as ze:
    print(ze)

# hangup participant
try:
    participant = conferencesConnector.hangupParticipant(
        'TestConferenceSid', 'TestParticipantSid')
    print(participant.callerNumber)
except ZangException as ze:
    print(ze)
