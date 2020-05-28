# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.base_node
~~~~~~~~~~~~~~~~~~~
This module contains BaseNode superclass for all inbound xml elements
"""

import sys
from enum import Enum

if sys.version_info > (3, 0):
    str_classes = (str, bytes)


class BaseNode(object):
    """Superclass for all inbound xml elements"""

    @property
    def attributes(self):
        """
        Get attributes dictionary from subclass vars that are not `None`

        Iterate over all subclass `vars` and filter those that are not `None`.
        Also skip `content` and `value` variables.
        :rtype: dict
        """
        attributes_ = {}
        for attribute in vars(self).keys():
            value = vars(self)[attribute]
            if (value is not None and attribute != '_content' and
                    attribute != '_value'):
                attributes_[attribute] = value
        return attributes_

    @property
    def xml(self):
        """
        Create a xml element with corresponding attributes and child elements.

        First get an openning xml tag from class name and local attributes
        dictionary. Than append content (if an element shuld have children),
        and at the end concate clsing tag.
        :rtype: str
        """
        className = self.__class__.__name__
        attributes_ = self.attributes
        s = self._createAttributesTag(className, attributes_)

        if len(type(self)._allowedContentClass) == 0 and self._value is None:
            s += '/>'
        else:
            s += '>' + self._createContent(
                className, self._content, self._value)
        return s

    def _createAttributesTag(self, className, attributes_):
        """
        Create an opening xml tag and append corresponding attributes.

        Using a class name, create opening xml tag and append attributes.
        If an attribute is a subclass of a `Enum`, get it's string value.
        :rtype: str
        """
        s = '<' + className
        for attribute in attributes_.keys():
            value = attributes_[attribute]
            if attribute == 'from_':
                attribute = 'from'
            if isinstance(value, Enum):
                value = value.value
            s += ' ' + attribute + '="' + str(value) + '"'
        return s

    def _createContent(self, className, content, value):
        """
        Create element content from child xml elements and given value.

        If an element has children, recursivly append their xml strings.
        At the end, append element's value.
        :rtype: str
        """
        s = ''
        if content is not None:
            for child in content:
                s += child if isinstance(child, str_classes) else child.xml

        if value is not None:
            s += str(value)

        s += ('</%s>' % className)
        return s
