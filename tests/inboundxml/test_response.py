import unittest
from zang.inboundxml.elements.response import Response
from zang.inboundxml.elements.dial import Dial
from zang.inboundxml.elements.say import Say
from zang.inboundxml.elements.constants import XML_DECLARATION


class TestResponse(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = XML_DECLARATION + '<Response></Response>'
        assert Response().xml == expected

    def test_init_add_element(self):
        number = '(555)555-5555'
        dial = Dial(number=number)
        text = 'Hello from Zang!'
        say = Say(text)
        response = Response()
        response.addElement(dial)
        response.addElement(say)
        expected = XML_DECLARATION + \
            '<Response><Dial>%s</Dial><Say>%s</Say></Response>' \
            % (number, text)
        assert response.xml == expected

    def test_init_remove_element_at_index(self):
        text = 'Hello from Zang!'
        say = Say(text)
        response = Response()
        response.addElement(say)

        expected = XML_DECLARATION + \
            '<Response><Say>%s</Say></Response>' % text
        assert response.xml == expected
        response.removeElementAtIndex(0)
        expected = XML_DECLARATION + '<Response></Response>'
        assert response.xml == expected

    def test_remove_element_at_out_of_range_index(self):
        text = 'Hello from Zang!'
        say = Say(text)
        response = Response()
        response.addElement(say)
        index = len(response._content)
        self.assertRaises(
            IndexError, lambda: response.removeElementAtIndex(index))

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Response(foo='bar'))

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(TypeError, lambda: Response().addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(AttributeError, lambda: Response().url)


if __name__ == '__main__':
    unittest.main()
