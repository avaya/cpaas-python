# -*- coding: utf-8 -*-

"""
zang.connectors.applications_connector
~~~~~~~~~~~~~~~~~~~
Module for communication with `Applications` endpoint
"""

from zang.connectors.base_connector import BaseConnector
from zang.helpers.helpers import flatDict

from zang.domain.application import Application
from zang.domain.list.applications import Applications


class ApplicationsConnector(BaseConnector):

    def __init__(self, executor):
        super(ApplicationsConnector, self).__init__(executor)

    def viewApplication(self, applicationSid):
        """
        Shows info on a TelAPI application.

        :param applicationSid: Application SID.
        :type applicationSid: str

        :return: `Application` object
        :rtype: zang.domain.application.Application
        :raises ZangException:
        """
        application = self._executor.read(
            ('Applications', applicationSid), Application)
        return application

    def listApplications(self, friendlyName=None, page=None, pageSize=None):
        """
        Shows info on all TelAPI applications associated with some account.

        :param friendlyName: (optional) Filters by the application's
            FriendlyName.
        :param page: (optional) Used to return a particular page within the
            list.
        :param pageSize: (optional) Used to specify the amount of list items
            to return per page.

        :type friendlyName: str
        :type page: int
        :type pageSize: int

        :return: `Applications` object
        :rtype: zang.domain.list.applications.Applications
        :raises ZangException:
        """
        queryParams = {
            'FriendlyName': friendlyName,
            'Page': page,
            'PageSize': pageSize,
        }
        params = flatDict(queryParams)
        applications = self._executor.read(
            ('Applications',), Applications, params=params)
        return applications

    def createApplication(
            self,
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
        Creates a new TelAPI application.


        :param friendlyName: (optional) The name used to identify This
            application. If this is not included at the initial POST, it
            is given the value of the application sid.
        :param voiceUrl: (optional) The URL requested once the call connects.
            This URL must be valid and should return InboundXML containing
            instructions on how to process your call. A badly formatted Url
            will NOT fallback to the FallbackUrl but return an error without
            placing the call. Url length is limited to 200 characters.
        :param voiceMethod: (optional) The HTTP method used to request the
            URL once the call connects. Valid parameters are GET and POST -
            any other value will default to POST.
        :param voiceFallbackUrl: (optional) URL used if the required URL is
            unavailable or if any errors occur during execution of the
            InboundXML returned by the required URL. Url length is limited
            to 200 characters.
        :param voiceFallbackMethod: (optional) The HTTP method used to
            request the FallbackUrl once the call connects. Valid parameters
            are GET and POST - any other value will default to POST.
        :param voiceCallerIdLookup: (optional) Look up the caller’s caller-ID
            name from the CNAM database (additional charges apply).
            Allowed values are "true" and "false".
        :param smsUrl: (optional) The URL requested when an SMS is received.
            This URL must be valid and should return InboundXML containing
            instructions on how to process the SMS. A badly formatted URL
            will NOT fallback to the FallbackUrl but return an error without
            placing the call. URL length is limited to 200 characters.
        :param smsMethod: (optional) The HTTP method used to request the
            URL when an SMS is received. Valid parameters are GET and
            POST - any other value will default to POST.
        :param smsFallbackUrl: (optional) URL used if the required URL is
            unavailable or if any errors occur during execution of the
            InboundXML returned by the required URL. Url length is
            limited to 200 characters.
        :param smsFallbackMethod: (optional) The HTTP method used to request
            the FallbackUrl once the call connects. Valid parameters are GET
            and POST - any other value will default to POST.
        :param heartbeatUrl: (optional) A URL that will be requested every
            60 seconds during the call, sending information about the call.
            The HeartbeatUrl will NOT be requested unless at least 60 seconds
            of call time have elapsed. URL length is limited to 200 characters.
        :param heartbeatMethod: (optional) The HTTP method used to request
            the HeartbeatUrl. Valid parameters are GET and POST - any other
            value will default to POST.
        :param statusCallback: (optional) A URL that will be requested when
            the call connects and ends, sending information about the call.
            URL length is limited to 200 characters.
        :param statusCallbackMethod: (optional) The HTTP method used to
            request the StatusCallback URL. Valid parameters are GET and
            POST - any other value will default to POST.
        :param hangupCallback: (optional) This is a StatusCallback clone
            that will be phased out in future versions.
        :param hangupCallbackMethod: (optional) This is a StatusCallbackMethod
            clone that will be phased out in future versions.

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

        :return: `Application` object
        :rtype: zang.domain.application.Application
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
        application = self._executor.create(
            ('Applications',), Application, data)
        return application

    def updateApplication(
            self,
            applicationSid,
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
        Updates TelAPI application data.

        :param ApplicationSid: Application SID
        :param FriendlyName: (optional) The name used to identify this
            application. If this is not included at the initial POST, it is
            given the value of the application sid.
        :param VoiceUrl: (optional) The URL requested once the call connects.
            This URL must be valid and should return InboundXML containing
            instructions on how to process your call. A badly formatted Url
            will NOT fallback to the FallbackUrl but return an error without
            placing the call. Url length is limited to 200 characters.
        :param VoiceMethod: (optional) The HTTP method used to request the
            URL once the call connects. Valid parameters are GET and
            POST - any other value will default to POST.
        :param VoiceFallbackUrl: (optional) URL used if the required URL is
            unavailable or if any errors occur during execution of the
            InboundXML returned by the required URL. URL length is limited to
            200 characters.
        :param VoiceFallbackMethod: (optional) The HTTP method used to request
            the FallbackUrl once the call connects. Valid parameters
            are GET and POST - any other value will default to POST.
        :param VoiceCallerIdLookup: (optional) Look up the caller’s caller-ID
            name from the CNAM database (additional charges apply).
            Allowed values are "true" and "false".
        :param SmsUrl: (optional) The URL requested when an SMS is received.
            This URL must be valid and should return InboundXML containing
            instructions on how to process the SMS. A badly formatted URL will
            NOT fallback to the FallbackUrl but return an error without
            placing the call. URL length is limited to 200 characters.
        :param SmsMethod: (optional) The HTTP method used to request the URL
            when an SMS is received. Valid parameters are GET and POST -
            any other value will default to POST.
        :param SmsFallbackUrl: (optional) URL used if the required URL is
            unavailable or if any errors occur during execution of the
            InboundXML returned by the required URL. URL length is limited to
            200 characters.
        :param SmsFallbackMethod: (optional) The HTTP method used to request
            the FallbackUrl once the call connects. Valid parameters are GET
            and POST - any other value will default to POST.
        :param HeartbeatUrl: (optional) A URL that will be requested every 60
            seconds during the call, sending information about the call. The
            HeartbeatUrl will NOT be requested unless at least 60 seconds of
            call time have elapsed. URL length is limited to 200 characters.
        :param HeartbeatMethod: (optional) The HTTP method used to request
            the HeartbeatUrl. Valid parameters are GET and POST - any other
            value will default to POST.
        :param StatusCallback: (optional) A URL that will be requested when
            the call connects and ends, sending information about the call.
            URL length is limited to 200 characters.
        :param StatusCallbackMethod: (optional) The HTTP method used to
            request the StatusCallback URL. Valid parameters are GET and
            POST - any other value will default to POST.
        :param HangupCallback: (optional) This is a StatusCallback clone that
            will be phased out in future versions.
        :param HangupCallbackMethod: (optional) This is a StatusCallbackMethod
            clone that will be phased out in future versions.

        :type ApplicationSid: str
        :type FriendlyName: str
        :type VoiceUrl: str
        :type VoiceMethod: zang.domain.enums.http_method.HttpMethod
        :type VoiceFallbackUrl: str
        :type VoiceFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type VoiceCallerIdLookup: bool
        :type SmsUrl: str
        :type SmsMethod: zang.domain.enums.http_method.HttpMethod
        :type SmsFallbackUrl: str
        :type SmsFallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type HeartbeatUrl: str
        :type HeartbeatMethod: zang.domain.enums.http_method.HttpMethod
        :type StatusCallback: str
        :type StatusCallbackMethod: zang.domain.enums.http_method.HttpMethod
        :type HangupCallback: str
        :type HangupCallbackMethod: zang.domain.enums.http_method.HttpMethod

        :return: `Application` object
        :rtype: zang.domain.application.Application
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
        application = self._executor.update(
            ('Applications', applicationSid), Application, data)
        return application

    def deleteApplication(self, applicationSid):
        """
        Deletes TelAPI application.

        :param applicationSid: Application SID.
        :type applicationSid: str

        :return: `Application` object
        :rtype: zang.domain.application.Application
        :raises ZangException:
        """
        application = self._executor.delete(
            ('Applications', applicationSid), Application)
        return application
