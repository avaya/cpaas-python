import unittest
from zang.inboundxml.elements.sip import Sip
from zang.inboundxml.elements.base_node import BaseNode


class TestSip(unittest.TestCase):

    def setUp(self):
        self.address = 'username@domain.com'

    def test_init_with_required_values(self):
        expected = '<Sip>' + self.address + '</Sip>'
        assert Sip(self.address).xml == expected

    def test_init_with_optional_attributes(self):
        sip = Sip(self.address, username='someusername')
        expected = '<Sip username="someusername">' + self.address + '</Sip>'
        assert sip.xml == expected

    def test_init_with_unsupported_attributes(self):
        """sip has no attribute foo"""
        self.assertRaises(TypeError, lambda: Sip(self.address, foo='bar'))

    def test_with_update_attributes(self):
        """test updating address and attributes"""
        sip = Sip(self.address)
        newAddress = 'newusername@domain.com'
        sip.address = newAddress
        sip.username = 'someusername'
        expected = '<Sip username="someusername">' + newAddress + '</Sip>'
        assert sip.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError, lambda: Sip(self.address).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError, lambda: Sip(self.address).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
