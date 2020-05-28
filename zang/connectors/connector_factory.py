from zang.http.executor import Executor
from zang.connectors.accounts_connector import AccountsConnector
from zang.connectors.applications_connector import ApplicationsConnector
from zang.connectors.sms_messages_connector import SmsMessagesConnector
from zang.connectors.mms_messages_connector import MmsMessagesConnector
from zang.connectors.calls_connector import CallsConnector
from zang.connectors.usages_connector import UsagesConnector
from zang.connectors.conferences_connector import ConferencesConnector
from zang.connectors.application_clients_connector import \
    ApplicationClientsConnector
from zang.connectors.sip_domains_connector import SipDomainsConnector
from zang.connectors.sip_credentials_connector import SipCredentialsConnector
from zang.connectors.transcriptions_connector import TranscriptionsConnector
from zang.connectors.recordings_connector import RecordingsConnector
from zang.connectors.notifications_connector import NotificationsConnector
from zang.connectors.available_phone_numbers_connector import \
    AvailablePhoneNumbersConnector
from zang.connectors.carrier_services_connector import CarrierServicesConnector
from zang.connectors.incoming_phone_numbers_connector import \
    IncomingPhoneNumbersConnector
from zang.connectors.ip_access_control_lists_connector import \
    IpAccessControlListsConnector
from zang.connectors.fraud_control_connector import FraudControlConnector


class ConnectorFactory(object):
    """The main Zang class."""

    def __init__(self, configuration=None, session=None):
        self.executor = Executor(session=session, configuration=configuration)

    @property
    def accountsConnector(self):
        return AccountsConnector(self.executor)

    @property
    def applicationsConnector(self):
        return ApplicationsConnector(self.executor)

    @property
    def smsMessagesConnector(self):
        return SmsMessagesConnector(self.executor)

    @property
    def mmsMessagesConnector(self):
        return MmsMessagesConnector(self.executor)

    @property
    def callsConnector(self):
        return CallsConnector(self.executor)

    @property
    def usagesConnector(self):
        return UsagesConnector(self.executor)

    @property
    def conferencesConnector(self):
        return ConferencesConnector(self.executor)

    @property
    def applicationClientsConnector(self):
        return ApplicationClientsConnector(self.executor)

    @property
    def sipDomainsConnector(self):
        return SipDomainsConnector(self.executor)

    @property
    def sipCredentialsConnector(self):
        return SipCredentialsConnector(self.executor)

    @property
    def transcriptionsConnector(self):
        return TranscriptionsConnector(self.executor)

    @property
    def recordingsConnector(self):
        return RecordingsConnector(self.executor)

    @property
    def notificationsConnector(self):
        return NotificationsConnector(self.executor)

    @property
    def availablePhoneNumbersConnector(self):
        return AvailablePhoneNumbersConnector(self.executor)

    @property
    def carrierServicesConnector(self):
        return CarrierServicesConnector(self.executor)

    @property
    def incomingPhoneNumbersConnector(self):
        return IncomingPhoneNumbersConnector(self.executor)

    @property
    def ipAccessControlListsConnector(self):
        return IpAccessControlListsConnector(self.executor)

    @property
    def fraudControlConnector(self):
        return FraudControlConnector(self.executor)
