# -*- coding: utf-8 -*-

"""
zang.connectors.usages_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Usages` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.usage import Usage
from zang.domain.list.usages import Usages


class UsagesConnector(BaseConnector):
    """
    Used for all forms of communication with the `Usages` endpoint of
        the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(UsagesConnector, self).__init__(executor)

    def viewUsage(self, usageSid):
        """
        View the usage of an item returned by List Usages.

        :return: `Usage` object
        :rtype: zang.domain.usage.Usage
        :raises ZangException:
        """
        usage = self._executor.read(('Usages', usageSid), Usage)
        return usage

    def listUsages(
            self,
            day=None,
            month=None,
            year=None,
            product=None,
            page=None,
            pageSize=None,):
        """
        Complete list of all usages of your account.

        :param day: (optional) Filters usage by day of month. If no month is
            specified then defaults to current month. Allowed values are
            integers between 1 and 31 depending on the month.
            Leading 0s will be ignored.
        :param month: (optional) ilters usage by month. Allowed values are
            integers between 1 and 12. Leading 0s will be ignored.
        :param year: (optional) Filters usage by year. Allowed values are
            valid years in integer form such as "2014".
        :param product: (optional) Filters usage by a specific “product” of
            TelAPI. Each product is uniquely identified by an integer.
            For example: Product=1, would return all outbound call usage.
            The integer assigned to each product is listed below.
        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type day: int
        :type month: int
        :type year: int
        :type product: int
        :type page: int
        :type pageSize: int

        :return: `Usages` object
        :rtype: zang.domain.list.usages.Usages
        :raises ZangException:
        """
        queryParams = {
            'Day': day,
            'Month': month,
            'Year': year,
            'Product': product,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        usageList = self._executor.read(('Usages', ), Usages, params=params)
        return usageList
