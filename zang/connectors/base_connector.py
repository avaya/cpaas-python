# -*- coding: utf-8 -*-

"""
zang.connectors.base_connector
~~~~~~~~~~~~~~~~~~~
This module contains base connector class used for all forms of communication
with the Zang REST API.
"""


class BaseConnector(object):

    def __init__(self, executor):
        """
        Creates a new ZangConnector

        :param executor: The http executor used for making API calls.
        :type executor: zang.http.executor.Executor
        """
        self._executor = executor
