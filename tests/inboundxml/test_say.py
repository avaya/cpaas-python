import unittest
from zang.inboundxml.elements.say import Say
from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.enums.voice import Voice


class TestSay(unittest.TestCase):

    def setUp(self):
        self.text = 'Hello from Zang'

    def test_init_with_required_values(self):
        expected = '<Say>' + self.text + '</Say>'
        assert Say(self.text).xml == expected

    def test_init_with_optional_attributes(self):
        loop = 100
        say = Say(self.text, loop=loop)
        expected = '<Say loop="%s">%s</Say>' % (loop, self.text)
        assert say.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Say(self.text, foo='bar'))

    def test_with_update_attributes(self):
        say = Say(self.text)
        text = 'Now I will not stop talking'
        voice = Voice.MALE
        say.text = text
        say.voice = voice
        expected = '<Say voice="%s">%s</Say>' % (voice.value, text)
        assert say.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Say(self.text).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Say(self.text).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
