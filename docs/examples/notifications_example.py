from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.log_level import LogLevel


from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
notificationsConnector = ConnectorFactory(configuration).notificationsConnector


# view notification
try:
    notification = notificationsConnector.viewNotification(
        "TestNotificationSid")
    print(notification.messageText)
except ZangException as ze:
    print(ze)


# list notifications
try:
    notifications = notificationsConnector.listNotifications(
        log=LogLevel.INFO, page=0, pageSize=33)
    if notifications and notifications.elements:
        for notification in notifications.elements:
            print(notification.messageText)
except ZangException as ze:
    print(ze)
