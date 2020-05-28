from zang.exceptions.zang_exception import ZangException

from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'


configuration = Configuration(sid, authToken, url=url)
ipAclConnector = ConnectorFactory(configuration).ipAccessControlListsConnector


# view ip access control list
try:
    ipAcl = ipAclConnector.viewIpAcl('TestIpAccessControlListSid')
    print(ipAcl.friendlyName)
except ZangException as ze:
    print(ze)


# list ip access control lists
try:
    ipAcls = ipAclConnector.listIpAcls(0, 33)
    print(ipAcls.total)
except ZangException as ze:
    print(ze)


# create ip access control list
try:
    ipAcl = ipAclConnector.createIpAcl('MyIpAclList')
    print(ipAcl.sid)
except ZangException as ze:
    print(ze)


# update ip access control list
try:
    ipAcl = ipAclConnector.updateIpAcl(
        'TestIpAccessControlListSid', 'NewIpAclList')
    print(ipAcl.friendlyName)
except ZangException as ze:
    print(ze)


# delete ip access control list
try:
    ipAcl = ipAclConnector.deleteIpAcl('TestIpAccessControlListSid')
    print(ipAcl.friendlyName)
except ZangException as ze:
    print(ze)


# view access control list ip
try:
    aclIp = ipAclConnector.viewAclIp(
        'TestIpAccessControlListSid', 'TestIpAddressSid')
    print(aclIp.friendlyName)
except ZangException as ze:
    print(ze)


# list access control list ips
try:
    aclIps = ipAclConnector.listAclIps('TestIpAccessControlListSid')
    print(aclIps.total)
except ZangException as ze:
    print(ze)


# add access contro list ip
try:
    aclIp = ipAclConnector.addAclIp(
        'TestIpAccessControlListSid', 'MyIpAddress', '10.0.0.1')
    print(aclIp.sid)
except ZangException as ze:
    print(ze)


# update access control list ip
try:
    aclIp = ipAclConnector.updateAclIp(
        'TestIpAccessControlListSid', 'TestIpAddressSid', 'NewIpAddress',
        '10.0.0.2')
    print(aclIp.friendlyName)
except ZangException as ze:
    print(ze)


# delete access control list ip
try:
    aclIp = ipAclConnector.deleteAclIp(
        'TestIpAccessControlListSid', 'TestIpAddressSid')
    print(aclIp.ipAddress)
except ZangException as ze:
    print(ze)
