import unittest
from zang.inboundxml.elements.sms import Sms
from zang.inboundxml.elements.base_node import BaseNode
from zang.domain.enums.http_method import HttpMethod


class TestSms(unittest.TestCase):

    def setUp(self):
        self.text = 'Hello from Zang'

    def test_init_with_required_values(self):
        expected = '<Sms>' + self.text + '</Sms>'
        assert Sms(self.text).xml == expected

    def test_init_with_optional_attributes(self):
        from_ = '+123456789'
        sms = Sms(self.text, from_=from_)
        expected = '<Sms from="%s">%s</Sms>' % (from_, self.text)
        assert sms.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Sms(self.text, foo='bar'))

    def test_with_update_attributes(self):
        sms = Sms(self.text)
        text = 'Now I will not stop talking'
        method = HttpMethod.GET
        sms.text = text
        sms.method = method
        expected = '<Sms method="%s">%s</Sms>' % (method.value, text)
        assert sms.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Sms(self.text).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Sms(self.text).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
