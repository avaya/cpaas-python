import unittest
from zang.inboundxml.elements.dial import Dial
from zang.domain.enums.http_method import HttpMethod
from zang.inboundxml.elements.number import Number


class TestDial(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Dial></Dial>'
        assert Dial().xml == expected

    def test_init_with_arguments(self):
        text = '(555)555-5555'
        dial = Dial(number=text)
        expected = '<Dial>%s</Dial>' % text
        assert dial.xml == expected

    def test_init_add_element(self):
        text = '(555)555-5555'
        number = Number(text)
        dial = Dial()
        dial.addElement(number)
        expected = '<Dial><Number>%s</Number></Dial>' % text
        assert dial.xml == expected

    def test_init_remove_element_at_index(self):
        text = 'Hello from Zang!'
        number = Number(text)
        dial = Dial()
        dial.addElement(number)
        expected = '<Dial><Number>%s</Number></Dial>' % text
        assert dial.xml == expected
        dial.removeElementAtIndex(0)
        expected = '<Dial></Dial>'
        assert dial.xml == expected

    def test_remove_element_at_out_of_range_index(self):
        text = 'Hello from Zang!'
        number = Number(text)
        dial = Dial()
        dial.addElement(number)
        index = len(dial._content)
        self.assertRaises(
            IndexError, lambda: dial.removeElementAtIndex(index))

    def test_init_with_optional_attributes(self):
        method = HttpMethod.GET
        dial = Dial(method=method)
        expected = '<Dial method="%s"></Dial>' % (method.value)
        assert dial.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Dial(foo='bar'))

    def test_with_update_attributes(self):
        dial = Dial()
        timeLimit = 0
        dial.timeLimit = 0
        expected = '<Dial timeLimit="%s"></Dial>' % (timeLimit)
        assert dial.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(TypeError, lambda: Dial().addElement(0.5))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(AttributeError, lambda: Dial().url)


if __name__ == '__main__':
    unittest.main()
