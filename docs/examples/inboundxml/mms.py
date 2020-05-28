
from zang.inboundxml import Response, Mms

from zang.domain.enums.http_method import HttpMethod

mms = Mms("https://tinyurl.com/lpewlmo",
          to="+123456",
          from_="+654321",
          method=HttpMethod.GET)

response = Response()
response.addElement(mms)

print(response.xml)
