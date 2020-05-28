from zang.domain.list.base_list import BaseList
from zang.domain.participant import Participant


class Participants(BaseList):

    _arrays = {'participants': Participant}

    def __init__(self):
        super(Participants, self).__init__()

    @property
    def elements(self):
        return self._participants
