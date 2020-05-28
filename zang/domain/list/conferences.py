from zang.domain.list.base_list import BaseList
from zang.domain.conference import Conference


class Conferences(BaseList):

    _arrays = {'conferences': Conference}

    def __init__(self):
        super(Conferences, self).__init__()

    @property
    def elements(self):
        return self._conferences
