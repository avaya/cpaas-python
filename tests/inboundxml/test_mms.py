import unittest
from zang.inboundxml.elements.mms import Mms
from zang.inboundxml.elements.base_node import BaseNode
from zang.domain.enums.http_method import HttpMethod


class TestMms(unittest.TestCase):

    def setUp(self):
        self.mediaUrl = 'https://tinyurl.com/lpewlmo'

    def test_init_with_required_values(self):
        expected = '<Mms mediaUrl="%s"/>' % (self.mediaUrl)
        assert Mms(self.mediaUrl).xml == expected

    def test_init_with_optional_attributes(self):
        from_ = '+123456789'
        mms = Mms(self.mediaUrl, from_=from_)
        expected = '<Mms from="%s" mediaUrl="%s"/>' % (from_, self.mediaUrl)
        assert mms.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Mms(self.mediaUrl, foo='bar'))

    def test_with_update_attributes(self):
        mms = Mms(self.mediaUrl)
        mediaUrl = 'https://media.giphy.com/media/zZJzLrxmx5ZFS/giphy.gif'
        text = 'Now I will not stop talking'
        method = HttpMethod.GET
        mms.mediaUrl = mediaUrl
        mms.text = text
        mms.method = method
        expected = '<Mms method="%s" mediaUrl="%s">%s</Mms>' % (method.value,mediaUrl, text)
        assert mms.xml == expected

    def test_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Mms(self.mediaUrl).addElement('bar'))

    def test_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Mms(self.mediaUrl).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
