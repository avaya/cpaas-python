from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.http_method import HttpMethod

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
applicationsConnector = ConnectorFactory(configuration).applicationsConnector


# view application
try:
    application = applicationsConnector.viewApplication('TestApplicationSid')
    print(application.friendlyName)
except ZangException as ze:
    print(ze)

# list applications
try:
    application = applicationsConnector.listApplications(
        'TestApplication', 0, 33)
    print(application.total)
except ZangException as ze:
    print(ze)

# create application
try:
    application = applicationsConnector.createApplication(
        friendlyName='TestApplication',
        voiceUrl='voiceUrl',
        voiceMethod=HttpMethod.POST,
        voiceFallbackUrl='voiceFallbackUrl',
        voiceFallbackMethod=HttpMethod.GET,
        voiceCallerIdLookup=True,
        smsUrl='smsUrl',
        smsMethod=HttpMethod.POST,
        smsFallbackUrl='smsFallbackUrl',
        smsFallbackMethod=HttpMethod.GET,
        heartbeatUrl='heartbeatUrl',
        heartbeatMethod=HttpMethod.GET,
        statusCallback='statusCallback',
        statusCallbackMethod=HttpMethod.POST,
        hangupCallback='hangupCallback',
        hangupCallbackMethod=HttpMethod.GET)
    print(application.sid)
except ZangException as ze:
    print(ze)

# update application
try:
    application = applicationsConnector.updateApplication(
        applicationSid='TestApplicationSid',
        friendlyName='TestApplication',
        voiceUrl='voiceUrl',
        voiceMethod=HttpMethod.POST,
        voiceFallbackUrl='voiceFallbackUrl',
        voiceFallbackMethod=HttpMethod.GET,
        voiceCallerIdLookup=True,
        smsUrl='smsUrl',
        smsMethod=HttpMethod.POST,
        smsFallbackUrl='smsFallbackUrl',
        smsFallbackMethod=HttpMethod.GET,
        heartbeatUrl='heartbeatUrl',
        heartbeatMethod=HttpMethod.GET,
        statusCallback='statusCallback',
        statusCallbackMethod=HttpMethod.POST,
        hangupCallback='hangupCallback',
        hangupCallbackMethod=HttpMethod.GET)
    print(application)
except ZangException as ze:
    print(ze)

# delete application
try:
    application = applicationsConnector.deleteApplication('TestApplicationSid')
    print(application.sid)
except ZangException as ze:
    print(ze)
