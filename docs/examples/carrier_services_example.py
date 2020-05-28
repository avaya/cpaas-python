from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
carrierServicesConnector = ConnectorFactory(
    configuration).carrierServicesConnector


# carrier lookup
try:
    data = carrierServicesConnector.viewCarrierLookup('+1234')
    print(data.network)
except ZangException as ze:
    print(ze)

# list carrier lookups
try:
    data = carrierServicesConnector.listCarrierLookups(0, 33)
    print(data.total)
except ZangException as ze:
    print(ze)

# cnam lookup
try:
    data = carrierServicesConnector.cnamLookup('+1234')
    print(data.phoneNumber)
except ZangException as ze:
    print(ze)

# list cnam lookups
try:
    data = carrierServicesConnector.listCnamLookups(0, 33)
    print(data.total)
except ZangException as ze:
    print(ze)

# bna lookup
try:
    data = carrierServicesConnector.bnaLookup('+1234')
    print(data.phoneNumber)
except ZangException as ze:
    print(ze)

# list bna lookups
try:
    data = carrierServicesConnector.listBnaLookups(0, 33)
    print(data.total)
except ZangException as ze:
    print(ze)
