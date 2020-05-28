from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory


from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
fraudControlConnector = ConnectorFactory(configuration).fraudControlConnector


# list fraud control resources
try:
    result = fraudControlConnector.listFraudControlResources(0, 33)
    print(result.total)
    if result and result.elements:
        for result in result.elements:
            print(result)
except ZangException as ze:
    print(ze)


# block destination
try:
    rule = fraudControlConnector.blockDestination('HR', False, True, False)
    print(rule.countryPrefix)
except ZangException as ze:
    print(ze)


# authorize destination
try:
    rule = fraudControlConnector.authorizeDestination('HR', False, True, False)
    print(rule.countryPrefix)
except ZangException as ze:
    print(ze)


# extend destination
try:
    rule = fraudControlConnector.extendDestinationAuthorization('HR')
    print(rule.expirationDate)
except ZangException as ze:
    print(ze)


# whitelist destination
try:
    rule = fraudControlConnector.whitelistDestination('HR', False, True, False)
    print(rule.countryPrefix)
except ZangException as ze:
    print(ze)
