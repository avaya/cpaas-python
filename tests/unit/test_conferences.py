import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.conference_status import ConferenceStatus
from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestConferences(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.conferencesConnector

    def test_view_conference(self):
        TestUtil.start('ConferencesTest', 'viewConference')
        conference = self.connector.viewConference('TestConferenceSid')
        self.checkConference(conference)

    def test_view_participant(self):
        TestUtil.start('ConferencesTest', 'viewParticipant')
        participant = self.connector.viewParticipant(
            'TestConferenceSid', 'TestParticipantSid')
        self.checkParticipant(participant)

    def test_mute_participant(self):
        TestUtil.start('ConferencesTest', 'muteDeafParticipant')
        participant = self.connector.deafOrMuteParticipant(
            'TestConferenceSid', 'TestParticipantSid', True, True)
        self.checkParticipant(participant)

    def test_play_audio_to_participant(self):
        TestUtil.start('ConferencesTest', 'playAudioToParticipant')
        participant = self.connector.playAudioToParticipant(
            'TestConferenceSid', 'TestParticipantSid',
            'http://mydomain.com/audio.mp3')
        self.checkParticipant(participant)

    def test_hangup_participant(self):
        TestUtil.start('ConferencesTest', 'hangupParticipant')
        participant = self.connector.hangupParticipant(
            'TestConferenceSid', 'TestParticipantSid')
        self.checkParticipant(participant)

    def tearDown(self):
        pass

    def checkConference(self, conference):
        assert conference.sid == 'TestConferenceSid'
        assert conference.friendlyName == 'TestConference'
        assert conference.status == ConferenceStatus.COMPLETED

    def checkParticipant(self, participant):
        assert participant.sid == 'TestParticipantSid'
        assert participant.conferenceSid == 'TestConferenceSid'
        assert not participant.muted
