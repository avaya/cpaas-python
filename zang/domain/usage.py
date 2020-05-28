# -*- coding: utf-8 -*-

"""
zang.domain.usage
~~~~~~~~~~~~~~~~~~~
`Usage` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.enums.product import Product


class Usage(BaseResource):

    _strs = [
        'sid',
        'uri',
    ]
    _ints = [
        'product_id',
        'day',
        'month',
        'year',
        'quantity',
    ]
    _reals = [
        'average_cost',
        'total_cost',
    ]

    _enums = {
        'product': Product,
    }

    def __init__(self):
        super(Usage, self).__init__()

    def __repr__(self):
        return '<Usage at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def product(self):
        """The product or feature used."""
        return self._product

    @property
    def uri(self):
        """The URL to this resource."""
        return self._uri

    @property
    def productId(self):
        """An integer identifying this product. You can see the full list
        under List Usage."""
        return self._product_id

    @property
    def day(self):
        """The day of the usage."""
        return self._day

    @property
    def month(self):
        """The month of the usage."""
        return self._month

    @property
    def year(self):
        """The year of the usage."""
        return self._year

    @property
    def quantity(self):
        """The quantity of the usage."""
        return self._quantity

    @property
    def averageCost(self):
        """The average cost of the usage."""
        return self._average_cost

    @property
    def totalCost(self):
        """The total cost of the usage."""
        return self._total_cost
