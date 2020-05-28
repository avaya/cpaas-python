# -*- coding: utf-8 -*-

"""
zang.connectors.conferences_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `MMS/Messages` endpoint
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.mms_message import MmsMessage


class MmsMessagesConnector(BaseConnector):
    """
    Used for all forms of communication with the `MMS/Messages`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(MmsMessagesConnector, self).__init__(executor)

    def sendMmsMessage(
            self,
            to,
            mediaUrl,
            body=None,
            from_=None,
            statusCallback=None,
            statusCallbackMethod=None):
        """
        Sends a MMS message.

        :param to: Must be an MMS capable number. The value does not have
            to be in any specific format.
        :param mediaUrl: URL of an image to be sent.
        :param body: Text of the MMS to be sent.
        :param from_: Must be a Zang number associated with your account.
            The value does not have to be in any specific format.
        :param statusCallback: The URL that will be sent information about
            the MMS. Url length is limited to 200 characters.
        :param statusCallbackMethod: The HTTP method used to request the
            StatusCallback. Valid parameters are GET and POST.

        :type to: str
        :type mediaUrl: str
        :type body: str
        :type from_: str
        :type statusCallback: str
        :type statusCallbackMethod: zang.domain.enums.http_method.HttpMethod

        :return: The MMS message which was sent.
        :rtype: domain.MmsMessage
        :raises: ZangException
        """
        bodyParams = {
            'To': to,
            'MediaUrl':mediaUrl,
            'Body': body,
            'From': from_,
            'StatusCallback': statusCallback,
            'StatusCallbackMethod': statusCallbackMethod
        }
        data = flatDict(bodyParams)
        mmsMessage = self._executor.create(
            ('MMS', 'Messages'), MmsMessage, data=data)
        return mmsMessage