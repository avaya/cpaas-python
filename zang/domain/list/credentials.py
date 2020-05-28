from zang.domain.list.base_list import BaseList
from zang.domain.credential import Credential


class Credentials(BaseList):

    _arrays = {'credentials': Credential}

    def __init__(self):
        super(Credentials, self).__init__()

    @property
    def elements(self):
        return self._credentials
