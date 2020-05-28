from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.exceptions.zang_exception import ZangException

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url)
accountsConnector = ConnectorFactory(configuration).accountsConnector

# view account
try:
    account = accountsConnector.viewAccount()
    print(account.friendlyName, account.accountBalance)
    print(account.subresourceUris.availablePhoneNumbers)
except ZangException as e:
    print(e)


# update account
try:
    accountsConnector.updateAccount('FriendlyName')
    print(account)
except ZangException as e:
    print(e)
