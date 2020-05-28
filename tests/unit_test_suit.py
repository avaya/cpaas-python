import unittest
from tests.unit.test_account import TestAccount
from tests.unit.test_application import TestApplication
from tests.unit.test_usages import TestUsages
from tests.unit.test_conferences import TestConferences
from tests.unit.test_mms_messages import TestMmsMessages
from tests.unit.test_sms_messages import TestSmsMessages
from tests.unit.test_calls import TestCalls
from tests.unit.test_transcriptions import TestTranscriptions
from tests.unit.test_sip_domain import TestSipDomain
from tests.unit.test_sip_credentials import TestSipCredentials
from tests.unit.test_recordings import TestRecordings
from tests.unit.test_notifications import TestNotifications
from tests.unit.test_application_clients import TestApplicationClients
from tests.unit.test_available_phone_number import TestAvailablePhoneNumber
from tests.unit.test_carrier_services import TestCarrierServices
from tests.unit.test_incoming_phone_numbers import TestIncomingPhoneNumbers
from tests.unit.test_ip_access_control_lists import TestIpAccessControlLists
from tests.unit.fraud_control_test import FraudControlTest


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FraudControlTest))
    test_suite.addTest(unittest.makeSuite(TestIpAccessControlLists))
    test_suite.addTest(unittest.makeSuite(TestIncomingPhoneNumbers))
    test_suite.addTest(unittest.makeSuite(TestAvailablePhoneNumber))
    test_suite.addTest(unittest.makeSuite(TestApplicationClients))
    test_suite.addTest(unittest.makeSuite(TestCarrierServices))
    test_suite.addTest(unittest.makeSuite(TestNotifications))
    test_suite.addTest(unittest.makeSuite(TestRecordings))
    test_suite.addTest(unittest.makeSuite(TestSipCredentials))
    test_suite.addTest(unittest.makeSuite(TestSipDomain))
    test_suite.addTest(unittest.makeSuite(TestTranscriptions))
    test_suite.addTest(unittest.makeSuite(TestCalls))
    test_suite.addTest(unittest.makeSuite(TestMmsMessages))
    test_suite.addTest(unittest.makeSuite(TestSmsMessages))
    test_suite.addTest(unittest.makeSuite(TestConferences))
    test_suite.addTest(unittest.makeSuite(TestUsages))
    test_suite.addTest(unittest.makeSuite(TestAccount))
    test_suite.addTest(unittest.makeSuite(TestApplication))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
