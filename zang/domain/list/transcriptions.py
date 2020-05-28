# -*- coding: utf-8 -*-

"""
zang.domain.list.transcriptions
~~~~~~~~~~~~~~~~~~~
`Transcriptions` model
"""

from zang.domain.list.base_list import BaseList
from zang.domain.transcription import Transcription


class Transcriptions(BaseList):

    _arrays = {'transcriptions': Transcription}

    def __init__(self):
        super(Transcriptions, self).__init__()

    @property
    def elements(self):
        return self._transcriptions
