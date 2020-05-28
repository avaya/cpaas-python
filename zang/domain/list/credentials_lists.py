from zang.domain.list.base_list import BaseList
from zang.domain.credentials_list import CredentialsList


class CredentialsLists(BaseList):

    _arrays = {'credential_lists': CredentialsList}

    def __init__(self):
        super(CredentialsLists, self).__init__()

    @property
    def elements(self):
        return self._credential_lists
