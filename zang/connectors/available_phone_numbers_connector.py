# -*- coding: utf-8 -*-

"""
zang.connectors.available_phone_numbers_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `AvailablePhoneNumbers` endpoint
"""
from enum import Enum

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.list.available_phone_numbers import AvailablePhoneNumbers


class AvailablePhoneNumbersConnector(BaseConnector):
    """
    Used for all forms of communication with the `AvailablePhoneNumbers`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def listAvailablePhoneNumbers(
            self,
            country,
            type_,
            page=None,
            pageSize=None,
            contains=None,
            areaCode=None,
            inRegion=None,
            inPostalCode=None,):
        """
        Shows information on all phone numbers available for purchasing

        :param country: Two letter country code.
        :param type_: Type of the phone number. Can be Local or Tollfree
        :param page: (optiona) Used to return a particular page within the
            list.
        :param pageSize: (optiona) Used to specify the amount of list items to
            return per page.
        :param contains: (optiona) Specifies the desired characters contained
            within the available numbers to list.
        :param areaCode: (optiona) Specifies the area code that the returned
            list of available numbers should be in. Only available for North
            American numbers
        :param inRegion: (optiona) Specifies the desired region of the
            available numbers to be listed.
        :param inPostalCode: (optiona) Specifies the desired postal code of the
            available numbers to be listed.

        :type country: str
        :type type: zang.domain.enums.available_number_type.AvailableNumberType
        :type page: int
        :type pageSize: int
        :type contains: str
        :type areaCode: str
        :type inRegion: str
        :type inPostalCode: str

        :return: `AvailablePhoneNumbers` object
        :rtype: zang.domain.list.available_phone_numbers.AvailablePhoneNumbers
        :raises ZangException:
        """
        queryParams = {
            'Country': country,
            'Type': type_,
            'Page': page,
            'PageSize': pageSize,
            'Contains': contains,
            'AreaCode': areaCode,
            'InRegion': inRegion,
            'InPostalCode': inPostalCode,
        }
        if isinstance(type_, Enum):
            type_ = type_.value
        params = flatDict(queryParams)
        availablePhoneNumbers = self._executor.read(
            ('AvailablePhoneNumbers', country, type_), AvailablePhoneNumbers,
            params)
        return availablePhoneNumbers
