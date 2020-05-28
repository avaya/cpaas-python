import unittest
from zang.inboundxml.elements.play_last_recording import PlayLastRecording
from zang.inboundxml.elements.base_node import BaseNode


class TestPlayLastRecording(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<PlayLastRecording/>'
        assert PlayLastRecording().xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(
            TypeError, lambda: PlayLastRecording('foo', bar='foobar'))

    def test_call_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: PlayLastRecording().addElement('bar'))

    def test_call_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError,
            lambda: PlayLastRecording(self.name).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
