import zang.configuration.constants as CONSTANTS


class Configuration(object):

    def __init__(self, sid, authToken, url=None):
        self.sid = sid
        self.authToken = authToken
        self.baseUrl = url if url is not None else CONSTANTS.BASE_URL
        self.proxyHost = None
        self.proxyPort = None
        self.proxyProtocol = None
