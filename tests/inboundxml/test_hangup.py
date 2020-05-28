import unittest
from zang.inboundxml.elements.hangup import Hangup
from zang.inboundxml.elements.enums.reject_reason import RejectReason
from zang.inboundxml.elements.base_node import BaseNode


class TestHangup(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Hangup/>'
        assert Hangup().xml == expected

    def test_init_with_optional_attributes(self):
        reason = RejectReason.BUSY
        hangup = Hangup(reason=reason)
        expected = '<Hangup reason="%s"/>' % reason.value
        assert hangup.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Hangup('foo', bar='foobar'))

    def test_with_update_attributes(self):
        reason = RejectReason.BUSY
        hangup = Hangup()
        hangup.reason = reason
        expected = '<Hangup reason="%s"/>' % (reason.value)
        assert hangup.xml == expected

    def test_call_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Hangup().addElement('bar'))

    def test_call_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Hangup(self.name).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
