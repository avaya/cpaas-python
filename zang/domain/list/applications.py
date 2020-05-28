from zang.domain.list.base_list import BaseList
from zang.domain.application import Application


class Applications(BaseList):

    _arrays = {'applications': Application}

    def __init__(self):
        super(Applications, self).__init__()

    @property
    def elements(self):
        return self._applications
