import unittest
from zang.inboundxml.elements.reject import Reject
from zang.inboundxml.elements.enums.reject_reason import RejectReason
from zang.inboundxml.elements.base_node import BaseNode


class TestReject(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Reject/>'
        assert Reject().xml == expected

    def test_init_with_optional_attributes(self):
        reason = RejectReason.BUSY
        reject = Reject(reason=reason)
        expected = '<Reject reason="%s"/>' % reason.value
        assert reject.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Reject('foo', bar='foobar'))

    def test_with_update_attributes(self):
        reason = RejectReason.BUSY
        reject = Reject(reason=reason)
        expected = '<Reject reason="%s"/>' % reason.value
        assert reject.xml == expected

    def test_call_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Reject().addElement('bar'))

    def test_call_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Reject(self.name).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
