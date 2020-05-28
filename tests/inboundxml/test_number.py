import unittest
from zang.inboundxml.elements.number import Number
from zang.inboundxml.elements.base_node import BaseNode


class TestNumber(unittest.TestCase):

    def setUp(self):
        self.number = '(555)555-555'

    def test_init_with_required_values(self):
        expected = '<Number>' + self.number + '</Number>'
        assert Number(self.number).xml == expected

    def test_init_with_optional_attributes(self):
        number = Number(self.number, sendDigits='ww12w3221')
        expected = '<Number sendDigits="ww12w3221">' + self.number + \
            '</Number>'
        assert number.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Number(self.number, foo='bar'))

    def test_with_update_attributes(self):
        number = Number(self.number)
        newNumber = 123456789
        number.number = newNumber
        number.sendDigits = 'ww12w3221'
        expected = '<Number sendDigits="ww12w3221">%s</Number>' % newNumber
        assert number.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Number(self.number).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Number(self.number).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
