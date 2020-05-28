from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector

# send sms message
try:
    smsMessage = smsMessagesConnector.sendSmsMessage(
        to='(XXX) XXX-XXXX',
        body='Hello from Zang!',
        from_='(XXX) XXX-XXXX')
    print(smsMessage)
except ZangException as e:
    print(e)


# view sms message
try:
    smsMessage = smsMessagesConnector.viewSmsMessage('SmsMessageSID')
    print(smsMessage.status)
except ZangException as e:
    print(e)


# list sms messages
try:
    smsMessages = smsMessagesConnector.listSmsMessages(
        dateSentGte=date(2016, 12, 31), dateSentLt=date(2017, 12, 31))
    print(smsMessages.total)
    for smsMessage in smsMessages.elements:
        print(smsMessage.sid, smsMessage.dateSent)
except ZangException as e:
    print(e)
