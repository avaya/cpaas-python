from zang.domain.list.base_list import BaseList
from zang.domain.call import Call


class Calls(BaseList):

    _arrays = {'calls': Call}

    def __init__(self):
        super(Calls, self).__init__()

    @property
    def elements(self):
        return self._calls
