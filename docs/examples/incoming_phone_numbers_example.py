from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
incomingPhoneNumbersConnector = ConnectorFactory(
    configuration).incomingPhoneNumbersConnector


# view incoming phone number
try:
    number = incomingPhoneNumbersConnector.viewIncomingPhoneNumber(
        'TestIncomingPhoneNumberSid')
    print(number.friendlyName)
except ZangException as ze:
    print(ze)


# list incoming phone numbers
try:
    numbers = incomingPhoneNumbersConnector.listIncomingPhoneNumbers(
        '123', 'MyNumber', 0, 25)
    print(numbers.total)
except ZangException as ze:
    print(ze)


# purchase incoming phone number
try:
    numbers = incomingPhoneNumbersConnector.purchaseIncomingPhoneNumber(
        friendlyName='MyNumber',
        areaCode='123',
        voiceCallerIdLookup=True,
        voiceApplicationSid='VoiceApplicationSid',
        smsApplicationSid='SmsApplicationSid')
    print(numbers.sid)
except ZangException as ze:
    print(ze)


# update incoming phone number
try:
    numbers = incomingPhoneNumbersConnector.updateIncomingPhoneNumber(
        'TestIncomingPhoneNumberSid', friendlyName='MyFavoriteNumber')
    print(numbers.friendlyName)
except ZangException as ze:
    print(ze)


# delete incoming phone number
try:
    numbers = incomingPhoneNumbersConnector.deleteIncomingPhoneNumber(
        'TestIncomingPhoneNumberSid')
    print(numbers.sid)
except ZangException as ze:
    print(ze)
