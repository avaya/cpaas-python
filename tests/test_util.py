try:
    import http.server
    import thread
    from urllib.parse import parse_qs
    from urllib.parse import urlencode
except ImportError:
    import http.server as BaseHTTPServer
    import _thread as thread
    # from urllib.parse import urlparse
    from urllib.parse import urlencode
    from urllib.parse import parse_qs
import sys
import json
import os

SID = 'TestAccountSid'
AUTH_TOKEN = 'TestToken'

PORT_NUMBER = 41123
URL = 'http://localhost:' + str(PORT_NUMBER)

RESOURCES_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'resources')
)
UNITTEST_PATH = os.path.join(RESOURCES_PATH, 'unittests.json')


class Expectation(object):

    def __init__(self, group, test):
        self._createExpectation(group, test)

    def _createExpectation(self, group, test):
        unittestsData = json.load(open(UNITTEST_PATH, 'r'))
        groupData = unittestsData[group]
        testData = groupData[test]
        # print(json.dumps(testData, indent=4, sort_keys=True))

        self.method = testData['method']

        if testData['path'] == 'Accounts':
            self.path = '/Accounts/' + SID + '.json'
        else:
            self.path = '/Accounts/' + SID + '/' + testData['path']

        self.queryParams = self._parseParams(testData['queryParams'])
        self.bodyParams = self._parseParams(testData['bodyParams'])
        self.responseFile = testData['response']

    def _parseParams(self, jsonParams):
        if jsonParams is None:
            return None
        params = {}
        for param in jsonParams:
            name = param['name']
            value = param['value']
            params[name] = value

        paramsUrlEncoded = urlencode(params)
        return paramsUrlEncoded


class MockHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self._process()

    def do_POST(self):
        self._process()

    def do_DELETE(self):
        self._process()

    def log_message(self, format, *args):
        return

    def _process(self):
        expectation = self.server.expectation
        bodyParams = self.bodyParams
        queryParams = self.queryParams

        # print(self.command, expectation.method,
        #       self.command == expectation.method)
        # print(self.pathWithoutQuery, expectation.path,
        #       self.pathWithoutQuery == expectation.path)
        # print('\nreceived bodyParams:', bodyParams)
        # print('\nexpected bodyParams:', expectation.bodyParams)
        # print('\nBody params ok:', self._isParamsEqual(
        #     bodyParams, expectation.bodyParams))
        # print('\nreceived queryParams:', queryParams)
        # print('\nexpected queryParams:', expectation.queryParams)
        # print('\nqueryParams ok:', self._isParamsEqual(
        #     queryParams, expectation.queryParams))

        if (self.command == expectation.method and
                self.pathWithoutQuery == expectation.path and
                self._isParamsEqual(bodyParams, expectation.bodyParams) and
                self._isParamsEqual(queryParams, expectation.queryParams)):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responsePath = RESOURCES_PATH + expectation.responseFile
            body = json.dumps(json.load(open(responsePath, 'r')))
            if sys.version_info >= (3, 0):
                body = str.encode(body)
            self.wfile.write(body)

    def _isParamsEqual(self, params0, params1):
        """Extract urlencoded string and compare all key value pairs if same"""
        if params0 == params1:
            return True
        elif params0 is None or params1 is None:
            return False

        try:
            dict0 = parse_qs(params0)
            dict1 = parse_qs(params1)
            for param in dict0:
                if param not in dict0.keys():
                    return False
                val0 = dict1[param][0]
                val1 = dict0[param][0]
                if val0.lower() == 'true' or val0.lower() == 'false':
                    val0 = bool(val0)
                    val1 = bool(val1)
                if val0 != val1:
                    return False
            return True
        except Expectation as e:
            print(e)
            return False

    @property
    def pathWithoutQuery(self):
        url = self.path.split('?')
        return None if len(url) == 0 else url[0]

    @property
    def bodyParams(self):
        if sys.version_info >= (3, 0):
            neadle = 'Content-Length'
        else:
            neadle = 'content-length'

        if (not hasattr(self, '_bodyParams') and
                neadle in self.headers.keys()):
            if sys.version_info >= (3, 0):
                contentLen = int(self.headers['Content-Length'])
            else:
                contentLen = int(self.headers.getheader('content-length', 0))

            if contentLen > 0:
                self._bodyParams = self.rfile.read(contentLen)
                if sys.version_info >= (3, 0):
                    self._bodyParams = self._bodyParams.decode('utf-8')
            else:
                self._bodyParams = None
        else:
            self._bodyParams = None
        return self._bodyParams

    @property
    def queryParams(self):
        url = self.path.split('?')
        return None if len(url) != 2 else url[1]


class MockHTTPServer(http.server.HTTPServer):

    def __init__(self, expectation, *args, **kw):
        http.server.HTTPServer.__init__(self, *args, **kw)
        self.expectation = expectation
        thread.start_new_thread(self.handle_request, ())


class TestUtil(object):

    @classmethod
    def start(cls, group, test):
        expectation = Expectation(group, test)
        serverAddress = ('', PORT_NUMBER)
        MockHTTPServer(expectation, serverAddress, MockHTTPRequestHandler)
