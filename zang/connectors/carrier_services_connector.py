# -*- coding: utf-8 -*-

"""
zang.connectors.carrier_services_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Carrier` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.carrier_lookup import CarrierLookup
from zang.domain.list.carrier_lookups import CarrierLookups

from zang.domain.cnam_lookup import CnamLookup
from zang.domain.list.cnam_lookups import CnamLookups

from zang.domain.bna_lookup import BnaLookup
from zang.domain.list.bna_lookups import BnaLookups


class CarrierServicesConnector(BaseConnector):
    """
    Used for all forms of communication with the `Lookups`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewCarrierLookup(self, phoneNumber):
        """
        The Carrier Lookup API allows you to retrieve additional information
        about a phone number.

        :param phoneNumber: Phone numbers to do a lookup for.
        :type phoneNumber: str

        :return: `CarrierLookup` object
        :rtype: zang.domain.carrier_lookup.CarrierLookup
        :raises ZangException:
        """
        bodyParams = {
            'PhoneNumber': phoneNumber,
        }
        data = flatDict(bodyParams)
        carrierLookup = self._executor.update(
            ('Lookups', 'Carrier'), CarrierLookup, data)
        return carrierLookup

    def listCarrierLookups(self, page=None, pageSize=None):
        """
        Shows info on all carrier lookups associated with some account

        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type page: int
        :type pageSize: int

        :return: `CarrierLookups` object
        :rtype: zang.domain.list.carrier_lookups.CarrierLookups
        :raises ZangException:
        """
        queryParams = {
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        carrierLookups = self._executor.read(
            ('Lookups', 'Carrier'), CarrierLookups, params)
        return carrierLookups

    def viewCnamLookup(self, phoneNumber):
        """
        Shows a CNAM information on some phone number

        :param phoneNumber: The number of the phone you are attempting to
            perform the CNAM lookup on. Multiple PhoneNumbers to lookup can
            be specified in a single request.
        :type phoneNumber: str

        :return: `CnamLookup` object
        :rtype: zang.domain.cnam_lookup.CnamLookup
        :raises ZangException:
        """
        bodyParams = {
            'PhoneNumber': phoneNumber,
        }
        data = flatDict(bodyParams)
        cnamLookup = self._executor.update(
            ('Lookups', 'Cnam'), CnamLookup, data)
        return cnamLookup

    def listCnamLookups(self, page=None, pageSize=None):
        """
        Shows info on all CNAM lookups associated with some account

        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type page: int
        :type pageSize: int

        :return: `CnamLookups` object
        :rtype: zang.domain.list.cnam_lookups.CnamLookups
        :raises ZangException:
        """
        queryParams = {
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        cnamLookups = self._executor.read(
            ('Lookups', 'Cnam'), CnamLookups, params)
        return cnamLookups

    def viewBnaLookup(self, phoneNumber):
        """
        Shows information on billing name address for some phone number.

        :param phoneNumber: The number of the phone you are attempting to
            perform the BNA lookup on. Multiple PhoneNumbers to lookup can be
            specified in a single request.
        :type phoneNumber: str

        :return: `BnaLookup` object
        :rtype: zang.domain.bna_lookup.BnaLookup
        :raises ZangException:
        """
        bodyParams = {
            'PhoneNumber': phoneNumber,
        }
        data = flatDict(bodyParams)
        bnaLookup = self._executor.update(
            ('Lookups', 'Bna'), BnaLookup, data)
        return bnaLookup

    def listBnaLookups(self, page=None, pageSize=None):
        """
        Shows info on all BNA lookups associated with some account.

        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type page: int
        :type pageSize: int

        :return: `BnaLookups` object
        :rtype: zang.domain.list.bna_lookups.BnaLookups
        :raises ZangException:
        """
        queryParams = {
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        bnaLookups = self._executor.read(
            ('Lookups', 'Bna'), BnaLookups, params)
        return bnaLookups
