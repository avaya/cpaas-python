# -*- coding: utf-8 -*-

"""
zang.connectors.conferences_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `SMS/Messages` endpoint
"""
from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.sms_message import SmsMessage
from zang.domain.list.sms_messages import SmsMessages


class SmsMessagesConnector(BaseConnector):
    """
    Used for all forms of communication with the `SMS/Messages`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def __init__(self, executor):
        super(SmsMessagesConnector, self).__init__(executor)

    def viewSmsMessage(self, smsMessageSid):
        """
        Text messages sent to and from Zang phone numbers are represented with.

        :param smsMessageSid:
        :type smsMessageSid: str

        :return: An Sms Message resource.
        :rtype: zang.domain.sms_message.SmsMessage
        :raises: ZangException
        """
        smsMessage = self._executor.read(
            ('SMS', 'Messages', smsMessageSid), SmsMessage)
        return smsMessage

    def listSmsMessages(
            self,
            to=None,
            from_=None,
            dateSentGte=None,
            dateSentLt=None,
            page=None,
            pageSize=None):
        """
        Text messages sent to and from Zang phone numbers are represented with.

        :param to: (optional) Lists all SMS messages sent to this number.
        :param from_: (optional) Lists all SMS messages sent from this number.
        :type dateSentGte: (optional) Filter by date sent greater or equal then
        :type dateSentLt: (optional) Filter by date sent less than
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type to: (optional) str
        :type from_: (optional) str
        :type dateSentGte: (optional) datetime.date
        :type dateSentLt: (optional) datetime.date
        :type page: (optional) int
        :type pageSize: (optional) int

        :return: A list of SmsMessage resources.
        :rtype: zang.domain.list.sms_messages.SmsMessages
        :raises: ZangException
        """
        queryParams = {
            'To': to,
            'From': from_,
            'DateSent>': dateSentGte,
            'DateSent<': dateSentLt,
            'Page': page,
            'PageSize': pageSize
        }
        params = flatDict(queryParams)
        smsMessageList = self._executor.read(
            ('SMS', 'Messages'), SmsMessages, params=params)
        return smsMessageList

    def sendSmsMessage(
            self,
            to,
            body,
            from_=None,
            statusCallback=None,
            statusCallbackMethod=None,
            allowMultiple=None):
        """
        Sends a SMS message.

        :param to: Must be an SMS capable number. The value does not have
            to be in any specific format.
        :param body: Text of the SMS to be sent.
        :param from_: Must be a Zang number associated with your account.
            The value does not have to be in any specific format.
        :param statusCallback: The URL that will be sent information about
            the SMS. Url length is limited to 200 characters.
        :param statusCallbackMethod: The HTTP method used to request the
            StatusCallback. Valid parameters are GET and POST.
        :param allowMultiple: If the Body length is greater than 160
            characters, the SMS will be sent as a multi-part SMS.
            Allowed values are True or False.

        :type to: str
        :type body: str
        :type from_: str
        :type statusCallback: str
        :type statusCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type allowMultiple: bool

        :return: The SMS message which was sent.
        :rtype: domain.SmsMessage
        :raises: ZangException
        """
        bodyParams = {
            'To': to,
            'Body': body,
            'From': from_,
            'StatusCallback': statusCallback,
            'StatusCallbackMethod': statusCallbackMethod,
            'AllowMultiple': allowMultiple,
        }
        data = flatDict(bodyParams)
        smsMessage = self._executor.create(
            ('SMS', 'Messages'), SmsMessage, data=data)
        return smsMessage
