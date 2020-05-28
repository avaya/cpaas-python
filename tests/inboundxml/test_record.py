import unittest
from zang.inboundxml.elements.record import Record
from zang.domain.enums.recording_file_format import RecordingFileFormat
from zang.inboundxml.elements.enums.record_direction import RecordDirection
from zang.inboundxml.elements.base_node import BaseNode


class TestRecord(unittest.TestCase):

    def test_init_with_required_values(self):
        expected = '<Record/>'
        assert Record().xml == expected

    def test_init_with_optional_attributes(self):
        fileFormat = RecordingFileFormat.MP3
        record = Record(fileFormat=fileFormat)
        expected = '<Record fileFormat="%s"/>' % fileFormat.value
        assert record.xml == expected

    def test_init_with_unsupported_attributes(self):
        self.assertRaises(TypeError, lambda: Record('foo', bar='foobar'))

    def test_with_update_attributes(self):
        direction = RecordDirection.IN
        record = Record()
        record.direction = direction
        expected = '<Record direction="%s"/>' % (direction.value)
        assert record.xml == expected

    def test_call_udefinded_method_with_primitive_type(self):
        self.assertRaises(
            AttributeError, lambda: Record().addElement('bar'))

    def test_call_udefinded_method_with_base_node(self):
        self.assertRaises(
            AttributeError, lambda: Record(self.name).addElement(BaseNode()))


if __name__ == '__main__':
    unittest.main()
