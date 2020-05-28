import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.available_number_type import AvailableNumberType

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestAvailablePhoneNumber(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.availablePhoneNumbersConnector

    def test_list_application_client(self):
        TestUtil.start(
            'AvailablePhoneNumbersTest', 'listAvailablePhoneNumbers')
        availablePhoneNumbers = self.connector.listAvailablePhoneNumbers(
            country='HR',
            type_=AvailableNumberType.TOLLFREE,
            contains='123',
            areaCode='052',
            inRegion='Istria',
            inPostalCode='52210',
            page=0,
            pageSize=20,)
        availablePhoneNumber = availablePhoneNumbers.elements[0]
        self.check_available_phone_number(availablePhoneNumber)

    def check_available_phone_number(self, availablePhoneNumber):
        assert availablePhoneNumber.isoCountry == 'HR'
