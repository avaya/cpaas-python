from zang.domain.base_resource import BaseResource


class Participant(BaseResource):

    _strs = [
        'sid',
        'caller_name',
        'conference_sid',
        'account_sid',
        'uri',
    ]
    _ints = [
        'caller_number',
        'duration',
    ]
    _dates = [
        'date_created',
        'date_updated',
    ]
    _bools = [
        'muted',
        'deaf',
    ]

    def __init__(self):
        super(Participant, self).__init__()

    def __repr__(self):
        return '<Participant at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this participant."""
        return self._sid

    @property
    def callerName(self):
        """The name displayed by the participant's caller ID."""
        return self._caller_name

    @property
    def conferenceSid(self):
        """The Sid identifying the conference this participant took part in."""
        return self._conference_sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account the conference
        participant is associated with."""
        return self._account_sid

    @property
    def uri(self):
        """The URL pointing to this resource."""
        return self._uri

    @property
    def callerNumber(self):
        """The number this participant used to call into the conference."""
        return self._caller_number

    @property
    def duration(self):
        """The duration in seconds that a participant has been in the
        conference."""
        return self._duration

    @property
    def dateCreated(self):
        """The date the conference participant resource was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the conference participant resource was last updated."""
        return self._date_updated

    @property
    def muted(self):
        """Boolean value indicating if this conference participant is
        currently muted."""
        return self._muted

    @property
    def deaf(self):
        """Boolean value indicating if this conference participant is
        currently deaf."""
        return self._deaf
