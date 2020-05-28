from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
applicationClientsConnector = ConnectorFactory(
    configuration).applicationClientsConnector


# view application client
try:
    applicationClient = applicationClientsConnector.viewApplicationClient(
        'TestApplicationSid', 'TestApplicationClientSid')
    print(applicationClient.nickname)
except ZangException as ze:
    print(ze)


# list application clients
try:
    applicationClients = applicationClientsConnector.listApplicationClients(
        'TestApplicationSid')
    print(applicationClients.total)
except ZangException as ze:
    print(ze)


# create application client
try:
    applicationClient = applicationClientsConnector.createApplicationClient(
        'TestApplicationSid', 'MyApplicationClient')
    print(applicationClient.sid)
except ZangException as ze:
    print(ze)
