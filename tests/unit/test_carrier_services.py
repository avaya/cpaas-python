import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestCarrierServices(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.connector = connectorFactory.carrierServicesConnector

    def test_carrier_lookup(self):
        TestUtil.start(
            'CarrierServicesTest', 'carrierLookup')

        carrierLookup = self.connector.viewCarrierLookup('+1234')
        assert carrierLookup.carrierId == 22607
        assert carrierLookup.countryCode == 'US'

    def test_list_carrier_lookups(self):
        TestUtil.start(
            'CarrierServicesTest', 'listCarrierLookups')
        carrierLookup = self.connector.listCarrierLookups(0, 33)
        assert len(carrierLookup.elements) == carrierLookup.total

    def test_cnam_lookup(self):
        TestUtil.start(
            'CarrierServicesTest', 'cnamLookup')

        cnamLookup = self.connector.viewCnamLookup('+1234')
        assert cnamLookup.phoneNumber == '+19093900002'

    def test_list_cnam_lookups(self):
        TestUtil.start(
            'CarrierServicesTest', 'listCnamLookups')
        cnamLookups = self.connector.listCnamLookups(0, 33)
        assert len(cnamLookups.elements) == cnamLookups.total

    def test_bna_lookup(self):
        TestUtil.start(
            'CarrierServicesTest', 'bnaLookup')

        bnaLookup = self.connector.viewBnaLookup('+1234')
        assert bnaLookup.phoneNumber == '+14086474636'

    def test_list_bna_lookups(self):
        TestUtil.start(
            'CarrierServicesTest', 'listBnaLookups')
        bnaLookups = self.connector.listBnaLookups(0, 33)
        assert len(bnaLookups.elements) == bnaLookups.total
