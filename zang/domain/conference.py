# -*- coding: utf-8 -*-

"""
zang.domain.conference
~~~~~~~~~~~~~~~~~~~
`Conference` model
"""
from zang.domain.base_resource import BaseResource
from zang.domain.enums.conference_status import ConferenceStatus


class Conference(BaseResource):

    _strs = [
        'sid',
        'friendly_name',
        'account_sid',
        'uri',
    ]
    _ints = [
        'active_participants_count',
        'run_time',
    ]
    _enums = {
        'status': ConferenceStatus,
    }

    def __init__(self):
        super(Conference, self).__init__()

    def __repr__(self):
        return '<Conference at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def friendlyName(self):
        """User generated name of the conference."""
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account the conference
        occurred through."""
        return self._account_sid

    @property
    def uri(self):
        """The URL for this resource."""
        return self._uri

    @property
    def activeParticipantsCount(self):
        """The number of participants currently connected to conference."""
        return self._active_participants_count

    @property
    def runTime(self):
        """Current conference duration in seconds."""
        return self._run_time

    @property
    def status(self):
        """Conference status. Possible values are “init”, “in-progress” or
        “completed”. “init” means the conference has been initialize, but
        no one has yet entered."""
        return self._status
