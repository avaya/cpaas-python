# -*- coding: utf-8 -*-

"""
zang.connectors.notifications_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Notifications` endpoint
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.notification import Notification
from zang.domain.list.notifications import Notifications


class NotificationsConnector(BaseConnector):
    """
    Used for all forms of communication with the `Notifications`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewNotification(self, notificationSid):
        """
        Shows information on some notification.

        :param notificationSid: Notification SID.
        :type notificationSid: str

        :return: `Notification` object
        :rtype: zang.domain.notification.Notification
        :raises ZangException:
        """
        notification = self._executor.read(
            ('Notifications', notificationSid), Notification)
        return notification

    def listNotifications(self, log=None, page=None, pageSize=None,):
        """
        Shows information on some notification.

        :param log: Specifies that only notifications with the given log level
            value should be listed. Allowed values are 1,2 or 3, where 2=INFO,
            1=WARNING, 0=ERROR.
        :param page: Used to return a particular page within the list.
        :param pageSize: Used to specify the amount of list items to return
            per page.

        :type log: zang.domain.enums.log_level.LogLevel
        :type page: int
        :type pageSize: int

        :return: `Notification` object
        :rtype: zang.domain.notification.Notification
        :raises ZangException:
        """
        queryParams = {
            'Log': log,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        notifications = self._executor.read(
            ('Notifications',), Notifications, params)
        return notifications
