import unittest
from zang.inboundxml.elements.play import Play
from zang.inboundxml.elements.base_node import BaseNode


class TestPlay(unittest.TestCase):

    def setUp(self):
        self.play = 'tone_stream://%(10000,0,350,440)'

    def test_init_with_required_values(self):
        expected = '<Play>' + self.play + '</Play>'
        assert Play(self.play).xml == expected

    def test_init_with_optional_attributes(self):
        play = Play(self.play, loop='100')
        expected = '<Play loop="100">' + self.play + \
            '</Play>'
        assert play.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Play(self.play, foo='bar'))

    def test_with_update_attributes(self):
        play = Play(self.play)
        newPlay = 'http://tone.url'
        play.url = newPlay
        play.loop = '100'
        expected = '<Play loop="100">%s</Play>' % newPlay
        assert play.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Play(self.play).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Play(self.play).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
