import unittest
from zang.inboundxml.elements.ping import Ping
from zang.inboundxml.elements.base_node import BaseNode


class TestPing(unittest.TestCase):

    def setUp(self):
        self.url = 'http://zang.io'

    def test_init_with_required_values(self):
        expected = '<Ping>' + self.url + '</Ping>'
        assert Ping(self.url).xml == expected

    def test_init_with_optional_attributes(self):
        ping = Ping(self.url, method='POST')
        expected = '<Ping method="POST">' + self.url + '</Ping>'
        assert ping.xml == expected

    def test_init_with_unsupported_attributes(self):
        """ping has no attribute foo"""
        self.assertRaises(TypeError, lambda: Ping(self.url, foo='bar'))

    def test_with_update_attributes(self):
        """test updating url and attributes"""
        ping = Ping(self.url)
        newUlr = 'http://bar'
        ping.url = newUlr
        ping.method = 'GET'
        expected = '<Ping method="GET">' + newUlr + '</Ping>'
        assert ping.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError, lambda: Ping(self.url).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError, lambda: Ping(self.url).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
