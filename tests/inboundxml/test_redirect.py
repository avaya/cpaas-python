import unittest
from zang.inboundxml.elements.redirect import Redirect
from zang.inboundxml.elements.base_node import BaseNode
from zang.domain.enums.http_method import HttpMethod


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.url = 'http://zang.io'

    def test_init_with_required_values(self):
        expected = '<Redirect>' + self.url + '</Redirect>'
        assert Redirect(self.url).xml == expected

    def test_init_with_optional_attributes(self):
        method = HttpMethod.POST
        redirect = Redirect(self.url, method=method)
        expected = '<Redirect method="%s">%s</Redirect>' \
            % (method.value, self.url)
        assert redirect.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Redirect(self.url, foo='bar'))

    def test_with_update_attributes(self):
        redirect = Redirect(self.url)
        newUrl = 'http://tone.url'
        method = HttpMethod.GET
        redirect.url = newUrl
        redirect.method = method
        expected = '<Redirect method="%s">%s</Redirect>' \
            % (method.value, newUrl)
        assert redirect.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Redirect(self.url).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Redirect(self.url).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
