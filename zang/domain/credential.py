from zang.domain.base_resource import BaseResource


class Credential(BaseResource):

    _strs = [
        'sid',
        'username',
        'friendly_name',
        'account_sid',
        'uri',
        'subresource_uris',
    ]
    _dates = ['date_created', 'date_updated', ]

    def __init__(self):
        super(Credential, self).__init__()

    def __repr__(self):
        return '<Credential at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def username(self):
        """Username associated with this credential."""
        return self._username

    @property
    def friendlyName(self):
        """A human-readable name for this credential."""
        return self._friendly_name

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with this
        resource."""
        return self._account_sid

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
        return self._uri

    @property
    def subresourceUris(self):
        """URIs for managing this resource."""
        return self._subresource_uris

    @property
    def dateCreated(self):
        """The date this credential was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date this credential was created."""
        return self._date_updated
