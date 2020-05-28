from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipCredentialsConnector = ConnectorFactory(
    configuration).sipCredentialsConnector


# view credentials list
try:
    credentialsList = sipCredentialsConnector.viewCredentialsList(
        'TestCredentialsListSid')
    print(credentialsList.credentialsCount)
except ZangException as ze:
    print(ze)


# list credentials lists
try:
    credentialsLists = sipCredentialsConnector.listCredentialsLists()
    print(credentialsLists.total)
except ZangException as ze:
    print(ze)


# create credentials list
try:
    credentialsList = sipCredentialsConnector.createCredentialsList(
        'MyCredentialsList')
    print(credentialsList.sid)
except ZangException as ze:
    print(ze)


# update credentials list
try:
    credentialsList = sipCredentialsConnector.updateCredentialsList(
        'TestCredentialsListSid', 'NewCredentialsList')
    print(credentialsList.friendlyName)
except ZangException as ze:
    print(ze)


# delete credentials list
try:
    credentialsList = sipCredentialsConnector.deleteCredentialsList(
        'TestCredentialsListSid')
    print(credentialsList.sid)
except ZangException as ze:
    print(ze)


# view credential
try:
    credential = sipCredentialsConnector.viewCredential(
        'TestCredentialsListSid', 'TestCredentialSid')
    print(credential.username)
except ZangException as ze:
    print(ze)


# list credentials
try:
    credentials = sipCredentialsConnector.listCredentials(
        'TestCredentialsListSid')
    print(credentials.total)
except ZangException as ze:
    print(ze)


# create credential
try:
    credential = sipCredentialsConnector.createCredential(
        'TestCredentialsListSid', 'testtest', 'testtestTEST123')
    print(credential.sid)
except ZangException as ze:
    print(ze)


# update credential
try:
    credential = sipCredentialsConnector.updateCredential(
        'TestCredentialsListSid', 'TestCredentialSid', 'TESTtesttest123')
    print(credential.username)
except ZangException as ze:
    print(ze)


# delete credential
try:
    credential = sipCredentialsConnector.deleteCredential(
        'TestCredentialsListSid', 'TestCredentialSid')
    print(credential.sid)
except ZangException as ze:
    print(ze)
