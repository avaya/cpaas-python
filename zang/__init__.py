# -*- coding: utf-8 -*-

"""
zang.py
~~~~~~~~~
:license: MIT, see LICENSE for more details.
"""

from .exceptions.zang_exception import ZangException  # NOQA
from .configuration.configuration import Configuration  # NOQA

# connectors
from .connectors.accounts_connector import AccountsConnector  # NOQA
from .connectors.application_clients_connector import \
    ApplicationClientsConnector  # NOQA
from .connectors.applications_connector import ApplicationsConnector  # NOQA
from .connectors.available_phone_numbers_connector import \
    AvailablePhoneNumbersConnector  # NOQA
from .connectors.calls_connector import CallsConnector  # NOQA
from .connectors.carrier_services_connector import \
    CarrierServicesConnector  # NOQA
from .connectors.conferences_connector import ConferencesConnector  # NOQA
from .connectors.connector_factory import ConnectorFactory  # NOQA
from .connectors.fraud_control_connector import FraudControlConnector  # NOQA
from .connectors.incoming_phone_numbers_connector import \
    IncomingPhoneNumbersConnector  # NOQA
from .connectors.ip_access_control_lists_connector import \
    IpAccessControlListsConnector  # NOQA
from .connectors.notifications_connector import NotificationsConnector  # NOQA
from .connectors.recordings_connector import RecordingsConnector  # NOQA
from .connectors.sip_credentials_connector import \
    SipCredentialsConnector  # NOQA
from .connectors.sip_domains_connector import SipDomainsConnector  # NOQA
from .connectors.sms_messages_connector import SmsMessagesConnector  # NOQA
from .connectors.transcriptions_connector import \
    TranscriptionsConnector  # NOQA
from .connectors.usages_connector import UsagesConnector  # NOQA

# enums
from .domain.enums.answered_by import AnsweredBy  # NOQA
from .domain.enums.audio_direction import AudioDirection  # NOQA
from .domain.enums.auth_type import AuthType  # NOQA
from .domain.enums.available_number_type import AvailableNumberType  # NOQA
from .domain.enums.call_direction import CallDirection  # NOQA
from .domain.enums.call_status import CallStatus  # NOQA
from .domain.enums.conference_status import ConferenceStatus  # NOQA
from .domain.enums.end_call_status import EndCallStatus  # NOQA
from .domain.enums.http_method import HttpMethod  # NOQA
from .domain.enums.if_machine import IfMachine  # NOQA
from .domain.enums.log_level import LogLevel  # NOQA
from .domain.enums.phone_number_type import PhoneNumberType  # NOQA
from .domain.enums.presence_status import PresenceStatus  # NOQA
from .domain.enums.product import Product  # NOQA
from .domain.enums.recording_audio_direction import \
    RecordingAudioDirection  # NOQA
from .domain.enums.recording_file_format import RecordingFileFormat  # NOQA
from .domain.enums.sms_direction import SmsDirection  # NOQA
from .domain.enums.sms_message_status import SmsMessageStatus  # NOQA
from .domain.enums.transcribe_quality import TranscribeQuality  # NOQA
from .domain.enums.transcription_status import TranscriptionStatus  # NOQA


__all__ = [
    'ZangException',
    'Configuration',
    # connectors
    'AccountsConnector',
    'ApplicationClientsConnector',
    'ApplicationsConnector',
    'AvailablePhoneNumbersConnector',
    'CallsConnector',
    'CarrierServicesConnector',
    'ConferencesConnector',
    'ConnectorFactory',
    'FraudControlConnector',
    'IncomingPhoneNumbersConnector',
    'IpAccessControlListsConnector',
    'NotificationsConnector',
    'RecordingsConnector',
    'SipCredentialsConnector',
    'SipDomainsConnector',
    'SmsMessagesConnector',
    'TranscriptionsConnector',
    'UsagesConnector',
    # enums
    'AnsweredBy',
    'AudioDirection',
    'AuthType',
    'AvailableNumberType',
    'CallDirection',
    'CallStatus',
    'ConferenceStatus',
    'EndCallStatus',
    'HttpMethod',
    'IfMachine',
    'LogLevel',
    'PhoneNumberType',
    'PresenceStatus',
    'Product',
    'RecordingAudioDirection',
    'RecordingFileFormat',
    'SmsDirection',
    'SmsMessageStatus',
    'TranscribeQuality',
    'TranscriptionStatus'
]

# meta

__title__ = 'zang'
__author__ = 'Zang'
__copyright__ = 'Copyright 2017 Zang'
__license__ = 'MIT'

__version__ = '1.0.0'
