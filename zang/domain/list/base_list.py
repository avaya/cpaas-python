from zang.domain.base_resource import BaseResource


class BaseList(BaseResource):

    _strs = [
        'uri',
        'first_page_uri',
        'previous_page_uri',
        'next_page_uri',
        'last_page_uri'
    ]
    _ints = [
        'page',
        'num_pages',
        'page_size',
        'total',
        'start',
        'end',
    ]

    def __init__(self):
        super(BaseList, self).__init__()

    @property
    def uri(self):
        return self._uri

    @property
    def firstPageUri(self):
        return self._first_page_uri

    @property
    def previousPageUri(self):
        return self._previous_page_uri

    @property
    def nextPageUri(self):
        return self._next_page_uri

    @property
    def lastPageUri(self):
        return self._last_page_uri

    @property
    def page(self):
        return self._page

    @property
    def numPages(self):
        return self._num_pages

    @property
    def pageSize(self):
        return self._page_size

    @property
    def total(self):
        return self._total

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end
