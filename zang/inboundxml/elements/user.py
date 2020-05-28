# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.user
~~~~~~~~~~~~~~~~~~~
Module containing `User` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode

import sys
if sys.version_info > (3, 0):
    str = (str, bytes)


class User(BaseNode):

    _allowedContentClass = (
        str,
    )

    def __init__(
            self,
            sendDigits=None,
            params=None,
    ):
        self.sendDigits = sendDigits
        self.params = params

        self._content = []
