import unittest
from zang.inboundxml.elements.gather import Gather
from zang.domain.enums.http_method import HttpMethod
from zang.inboundxml.elements.say import Say


class TestGather(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Gather></Gather>'
        assert Gather().xml == expected

    def test_init_add_element(self):
        text = 'Hello from Zang!'
        say = Say(text)
        gather = Gather()
        gather.addElement(say)
        expected = '<Gather><Say>%s</Say></Gather>' % text
        assert gather.xml == expected

    def test_init_remove_element_at_index(self):
        text = 'Hello from Zang!'
        say = Say(text)
        gather = Gather()
        gather.addElement(say)
        expected = '<Gather><Say>%s</Say></Gather>' % text
        assert gather.xml == expected
        gather.removeElementAtIndex(0)
        expected = '<Gather></Gather>'
        assert gather.xml == expected

    def test_remove_element_at_out_of_range_index(self):
        text = 'Hello from Zang!'
        say = Say(text)
        gather = Gather()
        gather.addElement(say)
        index = len(gather._content)
        self.assertRaises(
            IndexError, lambda: gather.removeElementAtIndex(index))

    def test_init_with_optional_attributes(self):
        method = HttpMethod.GET
        gather = Gather(method=method)
        expected = '<Gather method="%s"></Gather>' % (method.value)
        assert gather.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Gather(foo='bar'))

    def test_with_update_attributes(self):
        gather = Gather()
        numdigits = 0
        gather.numdigits = 0
        expected = '<Gather numdigits="%s"></Gather>' % (numdigits)
        assert gather.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(TypeError, lambda: Gather().addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(AttributeError, lambda: Gather().url)


if __name__ == '__main__':
    unittest.main()
