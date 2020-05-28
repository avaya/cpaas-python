from zang.domain.list.base_list import BaseList
from zang.domain.usage import Usage


class Usages(BaseList):

    _arrays = {'usages': Usage}

    def __init__(self):
        super(Usages, self).__init__()

    @property
    def elements(self):
        return self._usages
