from zang.domain.base_resource import BaseResource


class CredentialsList(BaseResource):

    _strs = [
        'sid',
        'account_sid',
        'friendly_name',
        'uri',
        'subresource_uris',
        'credentials',
    ]
    _ints = ['credentials_count']
    _dates = ['date_created', 'date_updated', ]

    def __init__(self):
        super(CredentialsList, self).__init__()

    def __repr__(self):
        return '<CredentialsList at 0x%x>' % (id(self))

    @property
    def sid(self):
        """An alphanumeric string identifying this resource."""
        return self._sid

    @property
    def accountSid(self):
        """An alphanumeric string identifying the account associated with this
        resource."""
        return self._account_sid

    @property
    def friendlyName(self):
        """A human-readable name associated with this domain."""
        return self._friendly_name

    @property
    def uri(self):
        """The Uniform Resource Identifier to this resource."""
        return self._uri

    @property
    def subresourceUris(self):
        """URIs for managing this resource."""
        return self._subresource_uris

    @property
    def credentials(self):
        """URI for managing credentials on this resource."""
        return self._credentials

    @property
    def dateCreated(self):
        """The date this credential list was created."""
        return self._date_created

    @property
    def dateUpdated(self):
        """The date the credential list was last updated."""
        return self._date_updated

    @property
    def credentialsCount(self):
        """Number of attached credentials."""
        return self._credentials_count
