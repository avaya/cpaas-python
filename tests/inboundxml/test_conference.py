import unittest
from zang.inboundxml.elements.conference import Conference
from zang.inboundxml.elements.base_node import BaseNode


class TestConference(unittest.TestCase):

    def setUp(self):
        self.name = 'ZangExampleConference'

    def test_init_with_required_values(self):
        expected = '<Conference>' + self.name + '</Conference>'
        assert Conference(self.name).xml == expected

    def test_init_with_optional_attributes(self):
        conference = Conference(self.name, beep=True)
        expected = '<Conference beep="True">' + self.name + '</Conference>'
        assert conference.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Conference(self.name, foo="bar"))

    def test_with_update_attributes(self):
        conference = Conference(self.name)
        newName = 'ExampleConferenceZang'
        conference.name = newName
        conference.beep = str(False)
        expected = '<Conference beep="False">' + newName + '</Conference>'
        assert conference.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError, lambda: Conference(self.name).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        """test calling undefined method"""
        self.assertRaises(
            AttributeError,
            lambda: Conference(self.name).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
