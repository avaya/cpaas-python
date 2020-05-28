import unittest
from tests.inboundxml.test_conference import TestConference
from tests.inboundxml.test_hangup import TestHangup
from tests.inboundxml.test_pause import TestPause
from tests.inboundxml.test_ping import TestPing
from tests.inboundxml.test_sip import TestSip
from tests.inboundxml.test_number import TestNumber
from tests.inboundxml.test_reject import TestReject
from tests.inboundxml.test_play import TestPlay
from tests.inboundxml.test_play_last_recording import TestPlayLastRecording
from tests.inboundxml.test_redirect import TestRedirect
from tests.inboundxml.test_say import TestSay
from tests.inboundxml.test_mms import TestMms
from tests.inboundxml.test_sms import TestSms
from tests.inboundxml.test_record import TestRecord
from tests.inboundxml.test_gather import TestGather
from tests.inboundxml.test_dial import TestDial
from tests.inboundxml.test_response import TestResponse


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestResponse))
    test_suite.addTest(unittest.makeSuite(TestDial))
    test_suite.addTest(unittest.makeSuite(TestGather))
    test_suite.addTest(unittest.makeSuite(TestSms))
    test_suite.addTest(unittest.makeSuite(TestMms))
    test_suite.addTest(unittest.makeSuite(TestRecord))
    test_suite.addTest(unittest.makeSuite(TestSay))
    test_suite.addTest(unittest.makeSuite(TestRedirect))
    test_suite.addTest(unittest.makeSuite(TestPlayLastRecording))
    test_suite.addTest(unittest.makeSuite(TestPlay))
    test_suite.addTest(unittest.makeSuite(TestReject))
    test_suite.addTest(unittest.makeSuite(TestConference))
    test_suite.addTest(unittest.makeSuite(TestHangup))
    test_suite.addTest(unittest.makeSuite(TestPause))
    test_suite.addTest(unittest.makeSuite(TestPing))
    test_suite.addTest(unittest.makeSuite(TestSip))
    test_suite.addTest(unittest.makeSuite(TestNumber))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
