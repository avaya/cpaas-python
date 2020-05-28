from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credetnials import sid, authToken

url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector


# view domain
try:
    domain = sipDomainsConnector.viewDomain('TestDomainSid')
    print(domain)
except ZangException as ze:
    print(ze)


# list domains
try:
    domains = sipDomainsConnector.listDomains()
    print(domains.total)
except ZangException as ze:
    print(ze)


# create domain
try:
    domain = sipDomainsConnector.createDomain(
        domainName='mydomain.com',
        friendlyName='MyDomain',
        voiceUrl='VoiceUrl',
        voiceMethod=HttpMethod.POST,
        voiceFallbackUrl='VoiceFallbackUrl',
        voiceFallbackMethod=HttpMethod.GET)
    print(domain.sid)
except ZangException as ze:
    print(ze)


# update domain
try:
    domain = sipDomainsConnector.updateDomain(
        'TestDomainSid',
        friendlyName='MyDomain3',
        voiceUrl='VoiceUrl2',
        voiceMethod=HttpMethod.POST,)
    print(domain.voiceUrl)
except ZangException as ze:
    print(ze)


# delete domain
try:
    domain = sipDomainsConnector.deleteDomain('TestDomainSid')
    print(domain.sid)
except ZangException as ze:
    print(ze)


# list mapped credentials lists
try:
    credentialsLists = sipDomainsConnector.listMappedCredentialsLists(
        'TestDomainSid')
    print(credentialsLists.total)
except ZangException as ze:
    print(ze)


# map credentials list
try:
    credentialsList = sipDomainsConnector.mapCredentialsLists(
        'TestDomainSid', 'TestCredentialsListSid')
    print(credentialsList.credentialsCount)
except ZangException as ze:
    print(ze)


# delete mapped credentials list
try:
    credentialsList = sipDomainsConnector.deleteMappedCredentialsList(
        'TestDomainSid', 'TestCredentialsListSid')
    print(credentialsList.friendlyName)
except ZangException as ze:
    print(ze)


# list mapped ip access control lists
try:
    aclLists = sipDomainsConnector.listMappedIpAccessControlLists(
        'TestDomainSid')
    print(aclLists.total)
except ZangException as ze:
    print(ze)


# map ip access control list
try:
    aclList = sipDomainsConnector.mapIpAccessControlList(
        'TestDomainSid', 'TestIpAccessControlListSid')
    print(aclList.credentialsCount)
except ZangException as ze:
    print(ze)


# delete mapped ip access control list
try:
    aclList = sipDomainsConnector.deleteMappedIpAccessControlList(
        'TestDomainSid', 'TestIpAccessControlListSid')
    print(aclList.friendlyName)
except ZangException as ze:
    print(ze)
