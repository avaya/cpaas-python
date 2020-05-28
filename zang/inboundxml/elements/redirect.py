# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.redirect
~~~~~~~~~~~~~~~~~~~
Module containing `Redirect` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode

import sys
if sys.version_info > (3, 0):
    str = (str, bytes)


class Redirect(BaseNode):

    _allowedContentClass = (
        str,
    )

    def __init__(self, url, method=None):
        if url is None:
            raise TypeError
        self.method = method
        self._value = url
        self._content = []

    @property
    def url(self):
        return self._value

    @url.setter
    def url(self, value):
        if value is None:
            raise TypeError
        self._value = value
