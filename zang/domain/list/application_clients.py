from zang.domain.list.base_list import BaseList
from zang.domain.application_client import ApplicationClient


class ApplicationClients(BaseList):

    _arrays = {'clients': ApplicationClient}

    def __init__(self):
        super(ApplicationClients, self).__init__()

    @property
    def elements(self):
        return self._clients
