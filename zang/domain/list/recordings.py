# -*- coding: utf-8 -*-

"""
zang.domain.list.recordings
~~~~~~~~~~~~~~~~~~~
`Recordings` model
"""
from zang.domain.list.base_list import BaseList
from zang.domain.recording import Recording


class Recordings(BaseList):

    _arrays = {'recordings': Recording}

    def __init__(self):
        super(Recordings, self).__init__()

    @property
    def elements(self):
        return self._recordings
