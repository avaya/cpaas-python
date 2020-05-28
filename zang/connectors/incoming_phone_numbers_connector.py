# -*- coding: utf-8 -*-

"""
zang.connectors.incoming_phone_numbers_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Incoming Phone Numbers` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.incoming_phone_number import IncomingPhoneNumber
from zang.domain.list.incoming_phone_numbers import IncomingPhoneNumbers


class IncomingPhoneNumbersConnector(BaseConnector):
    """
    Used for all forms of communication with the `Incoming Phone Numbers`
    endpoint of the Zang REST API.
    .. seealso:: zang.connectors.connector_factory.ConnectorFactory
    """

    def viewIncomingPhoneNumber(self, incomingNumberSid):
        """
        Shows info on an incoming phone number.

        :param incomingNumberSid: Incoming number SID.
        :type incomingNumberSid: str

        :return: `IncomingPhoneNumber` object
        :rtype: zang.domain.incoming_phone_number.IncomingPhoneNumber
        :raises ZangException:
        """
        incomingPhoneNumber = self._executor.read(
            ('IncomingPhoneNumbers', incomingNumberSid), IncomingPhoneNumber)
        return incomingPhoneNumber

    def listIncomingPhoneNumbers(
            self,
            contains=None,
            friendlyName=None,
            page=None,
            pageSize=None,):
        """
        Shows info on all incoming numbers associated with some account

        :param contains: List numbers containing certain digits.
        :param friendlyName: Specifies that only IncomingPhoneNumber resources
            matching the input FriendlyName should be returned in the list
            request.
        :param page: Used to return a particular page within the list.
        :param pageSize: Used to specify the amount of list items to return
            per page.

        :type contains: str
        :type friendlyName: str
        :type page: int
        :type pageSize: int

        :return: `IncomingPhoneNumbers` object
        :rtype: zang.domain.incoming_phone_numbers.IncomingPhoneNumbers
        :raises ZangException:
        """
        queryParams = {
            'Contains': contains,
            'FriendlyName': friendlyName,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        incomingPhoneNumbers = self._executor.read(
            ('IncomingPhoneNumbers',), IncomingPhoneNumbers, params)
        return incomingPhoneNumbers

    def purchaseIncomingPhoneNumber(
            self,
            phoneNumber=None,
            areaCode=None,
            friendlyName=None,
            voiceUrl=None,
            voiceMethod=None,
            voiceFallbackUrl=None,
            voiceFallbackMethod=None,
            voiceCallerIdLookup=None,
            smsUrl=None,
            smsMethod=None,
            smsFallbackUrl=None,
            smsFallbackMethod=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            statusCallback=None,
            statusCallbackMethod=None,
            hangupCallback=None,
            hangupCallbackMethod=None,
            voiceApplicationSid=None,
            smsApplicationSid=None,):
        """
        Purchases a new incoming number.

        :param phoneNumber: A specific available phone number you wish to add.
        :param areaCode:The area code from which a random available number will
            be added.
        :param friendlyName:User generated name for the incoming number.
        :param voiceUrl:The URL returning InboundXML incoming calls should
            execute when connected.
        :param voiceMethod: Specifies the HTTP method used to request the
            VoiceUrl once incoming call connects.
        :param voiceFallbackUrl:URL used if any errors occur during execution
            of InboundXML on a call or at initial request of the VoiceUrl.
        :param voiceFallbackMethod: Specifies the HTTP method used to request
            the VoiceFallbackUrl once incoming call connects.
        :param voiceCallerIdLookup: Look up the caller’s caller-ID name forms
            the CNAM database (additional charges apply).
        :param smsUrl: The URL returning InboundXML incoming phone numbers
            should execute when receiving an SMS.
        :param smsMethod: Specifies the HTTP method used to request the smsUrl
            once an incoming SMS is received.
        :param smsFallbackUrl: URL used if any errors occur during execution
            of InboundXML from an SMS or at initial request of the SmsUrl.
        :param smsFallbackMethod: Specifies the HTTP method used to request
            the SmsFallbackUrl.
        :param heartbeatUrl:URL that can be used to monitor the phone number.
        :param heartbeatMethod: The HTTP method TelAPI will use when
            requesting the HeartbeatURL.
        :param statusCallback: URL that can be requested to receive
            notification when and how incoming call has ended.
        :param statusCallbackMethod:The HTTP method TelAPI will use when
            requesting the HangupCallback URL.
        :param hangupCallback: This is a StatusCallback clone that will be
            phased out in future versions.
        :param hangupCallbackMethod:This is a StatusCallbackMethod clone that
            will be phased out in future versions.
        :param voiceApplicationSid: The SID of the Voice Application you wish
            to associate with this incoming number.
        :param smsApplicationSid: The SID of the SMS Application you wish to
            associate with this incoming number.

        :type phoneNumber: str
        :type areaCode: str
        :type friendlyName: str
        :type voiceUrl: String
        :type voiceMethod: zang.domain.enums.http_method.HttpMethod
        :type voiceFallbackUrl: String
        :type voiceFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type voiceCallerIdLookup: bool
        :type smsUrl: String
        :type smsMethod: zang.domain.enums.http_method.HttpMethod
        :type smsFallbackUrl: String
        :type smsFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type heartbeatUrl: String
        :type heartbeatMethod: zang.domain.enums.http_method.HttpMethod
        :type statusCallback: String
        :type statusCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type hangupCallback:  String
        :type hangupCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type voiceApplicationSid: String
        :type smsApplicationSid: String

        :return: `IncomingPhoneNumber` object
        :rtype: zang.domain.incoming_phone_number.IncomingPhoneNumber
        :raises ZangException:
        """
        bodyParams = {
            'PhoneNumber': phoneNumber,
            'AreaCode': areaCode,
            'FriendlyName': friendlyName,
            'VoiceUrl': voiceUrl,
            'VoiceMethod': voiceMethod,
            'VoiceFallbackUrl': voiceFallbackUrl,
            'VoiceFallbackMethod': voiceFallbackMethod,
            'VoiceCallerIdLookup': voiceCallerIdLookup,
            'SmsUrl': smsUrl,
            'SmsMethod': smsMethod,
            'SmsFallbackUrl': smsFallbackUrl,
            'SmsFallbackMethod': smsFallbackMethod,
            'HeartbeatUrl': heartbeatUrl,
            'HeartbeatMethod': heartbeatMethod,
            'StatusCallback': statusCallback,
            'StatusCallbackMethod': statusCallbackMethod,
            'HangupCallback': hangupCallback,
            'HangupCallbackMethod': hangupCallbackMethod,
            'VoiceApplicationSid': voiceApplicationSid,
            'SmsApplicationSid': smsApplicationSid,
        }
        data = flatDict(bodyParams)
        incomingPhoneNumber = self._executor.create(
            ('IncomingPhoneNumbers',), IncomingPhoneNumber, data)
        return incomingPhoneNumber

    def updateIncomingPhoneNumber(
            self,
            incomingPhoneNumberSid,
            friendlyName=None,
            voiceUrl=None,
            voiceMethod=None,
            voiceFallbackUrl=None,
            voiceFallbackMethod=None,
            voiceCallerIdLookup=None,
            smsUrl=None,
            smsMethod=None,
            smsFallbackUrl=None,
            smsFallbackMethod=None,
            heartbeatUrl=None,
            heartbeatMethod=None,
            statusCallback=None,
            statusCallbackMethod=None,
            hangupCallback=None,
            hangupCallbackMethod=None,):
        """
        Updates an incoming phone number data

        :param incomingNumberSid: Incoming number SID.
        :param friendlyName: User generated name for the incoming number.
        :param voiceUrl: The URL returning InboundXML incoming calls should
            execute when connected.
        :param voiceMethod: Specifies the HTTP method used to request the
            VoiceUrl once incoming call connects.
        :param voiceFallbackUrl: URL used if any errors occur during execution
            of InboundXML on a call or at initial request of the VoiceUrl.
        :param voiceFallbackMethod: Specifies the HTTP method used to request
            the VoiceFallbackUrl once incoming call connects.
        :param voiceCallerIdLookup: Look up the caller’s caller-ID name from
            the CNAM database (additional charges apply).
        :param smsUrl: The URL returning InboundXML incoming phone numbers
            should execute when receiving an SMS.
        :param smsMethod: Specifies the HTTP method used to request the SmsUrl
            once an incoming SMS is received.
        :param smsFallbackUrl: URL used if any errors occur during execution
            of InboundXML from an SMS or at initial request of the SmsUrl.
        :param smsFallbackMethod: Specifies the HTTP method used to request
            the SmsFallbackUrl.
        :param heartbeatUrl: URL that can be used to monitor the phone number.
        :param heartbeatMethod: The HTTP method TelAPI will use when
            requesting the HeartbeatURL.
        :param statusCallback: URL that can be requested to receive
            notification when and how incoming call has ended.
        :param statusCallbackMethod: The HTTP method TelAPI will use when
            requesting the HangupCallback URL.
        :param hangupCallback: This is a StatusCallback clone that will be
            phased out in future versions.
        :param hangupCallbackMethod: This is a StatusCallbackMethod clone that
            will be phased out in future versions.

        :type incomingNumberSid: str
        :type friendlyName: str
        :type voiceUrl: str
        :type voiceMethod: zang.domain.enums.http_method.HttpMethod
        :type voiceFallbackUrl: str
        :type voiceFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type voiceCallerIdLookup: bool
        :type smsUrl: str
        :type smsMethod: zang.domain.enums.http_method.HttpMethod
        :type smsFallbackUrl: str
        :type smsFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type heartbeatUrl: str
        :type heartbeatMethod: zang.domain.enums.http_method.HttpMethod
        :type statusCallback: str
        :type statusCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type hangupCallback: str
        :type hangupCallbackMethod: zang.domain.enums.http_method.HttpMethod

        :return: `IncomingPhoneNumber` object
        :rtype: zang.domain.incoming_phone_number.IncomingPhoneNumber
        :raises ZangException:
        """
        bodyParams = {
            'FriendlyName': friendlyName,
            'VoiceUrl': voiceUrl,
            'VoiceMethod': voiceMethod,
            'VoiceFallbackUrl': voiceFallbackUrl,
            'VoiceFallbackMethod': voiceFallbackMethod,
            'VoiceCallerIdLookup': voiceCallerIdLookup,
            'SmsUrl': smsUrl,
            'SmsMethod': smsMethod,
            'SmsFallbackUrl': smsFallbackUrl,
            'SmsFallbackMethod': smsFallbackMethod,
            'HeartbeatUrl': heartbeatUrl,
            'HeartbeatMethod': heartbeatMethod,
            'StatusCallback': statusCallback,
            'StatusCallbackMethod': statusCallbackMethod,
            'HangupCallback': hangupCallback,
            'HangupCallbackMethod': hangupCallbackMethod,
        }
        data = flatDict(bodyParams)
        incomingPhoneNumber = self._executor.update(
            ('IncomingPhoneNumbers', incomingPhoneNumberSid),
            IncomingPhoneNumber, data)
        return incomingPhoneNumber

    def deleteIncomingPhoneNumber(self, incomingNumberSid):
        """
        Deletes an incoming phone number

        :param incomingNumberSid: Incoming number SID.
        :type incomingNumberSid: str

        :return: `IncomingPhoneNumber` object
        :rtype: zang.domain.incoming_phone_number.IncomingPhoneNumber
        :raises ZangException:
        """
        incomingPhoneNumber = self._executor.delete(
            ('IncomingPhoneNumbers', incomingNumberSid), IncomingPhoneNumber)
        return incomingPhoneNumber
