from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.available_number_type import AvailableNumberType

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
availablePhoneNumbersConnector = ConnectorFactory(
    configuration).availablePhoneNumbersConnector

try:
    numbers = availablePhoneNumbersConnector.listAvailablePhoneNumbers(
        country="HR",
        type_=AvailableNumberType.TOLLFREE,
        contains="123",
        areaCode="052",
        inRegion="Istria",
        inPostalCode="52210",
        page=0,
        pageSize=20)
    print(numbers.total)
except ZangException as ze:
    print(ze)
