from zang.domain.list.base_list import BaseList
from zang.domain.sms_message import SmsMessage


class SmsMessages(BaseList):

    _arrays = {'sms_messages': SmsMessage}

    def __init__(self):
        super(SmsMessages, self).__init__()

    @property
    def elements(self):
        return self._sms_messages
