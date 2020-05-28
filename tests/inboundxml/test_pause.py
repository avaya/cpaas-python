import unittest
from zang.inboundxml.elements.pause import Pause
from zang.inboundxml.elements.base_node import BaseNode


class TestPause(unittest.TestCase):

    def test_init_without_attributes(self):
        pause = Pause()
        assert pause.xml == '<Pause/>'

    def test_init_with_attributes(self):
        pause = Pause(length=1)
        assert pause.xml == '<Pause length="1"/>'

    def test_init_update_attributes(self):
        pause = Pause(length=2)
        pause.length = 3
        assert pause.xml == '<Pause length="3"/>'

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Pause(foo='bar'))

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(AttributeError, lambda: Pause().addElement('foo'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Pause().addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
