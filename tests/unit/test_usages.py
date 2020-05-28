import unittest

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.product import Product
from tests.test_util import TestUtil, SID, AUTH_TOKEN, URL


class TestUsages(unittest.TestCase):

    def setUp(self):
        configuration = Configuration(SID, AUTH_TOKEN, URL)
        connectorFactory = ConnectorFactory(configuration)
        self.usagesConnector = connectorFactory.usagesConnector

    def test_view(self):
        TestUtil.start('UsagesTest', 'viewUsage')
        usage = self.usagesConnector.viewUsage('TestUsageSid')
        assert usage.sid == 'AU61196f97109e11e7bf6bd0cc8f654d53'
        assert usage.quantity == 120

    def test_list(self):
        TestUtil.start('UsagesTest', 'listUsages')
        usages = self.usagesConnector.listUsages(
            page=0,
            pageSize=25,
            product=3,
            day=12,
            month=12,
            year=2016,)
        assert usages.uri == \
            "/v2/Accounts/ACe1889084056167d57a944486a50ceb46/Usages.json"
        assert usages.elements[0].sid == 'AU61196f97109e11e7bf6bd0cc8f654d53'
        assert usages.elements[0].product == Product.TRANSCRIPTION_AUTO

    def tearDown(self):
        pass
