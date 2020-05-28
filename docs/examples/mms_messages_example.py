from datetime import date

from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
mmsMessagesConnector = ConnectorFactory(configuration).mmsMessagesConnector

# send sms message
try:
    mmsMessage = mmsMessagesConnector.sendMmsMessage(
        to='(XXX) XXX-XXXX',
        mediaUrl="https://media.giphy.com/media/zZJzLrxmx5ZFS/giphy.gif",
        body='This is MMS sent from Zang',
        from_='(XXX) XXX-XXXX',
        statusCallback='callback.url')
    print(mmsMessage)
except ZangException as e:
    print("in exception")
    print(e)
