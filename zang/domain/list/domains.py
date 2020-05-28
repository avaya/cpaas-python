from zang.domain.list.base_list import BaseList
from zang.domain.domain import Domain


class Domains(BaseList):

    _arrays = {'domains': Domain}

    def __init__(self):
        super(Domains, self).__init__()

    @property
    def elements(self):
        return self._domains
