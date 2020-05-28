from zang.inboundxml import Response, Gather, Say

from zang.domain.enums.http_method import HttpMethod
from zang.inboundxml import Voice, Language, BCPLanguage, GatherInput

gather = Gather("http://example.com/example-callback-url/say?example=simple.xml",
                method=HttpMethod.GET,
                timeout=10,
                finishOnKey="#",
                numDigits=4,
                hints="sales",
                input=GatherInput.SPEECH,
                language=BCPLanguage.EN_IN)

say = Say("Please say sales for sales.",
          language=Language.EN,
          voice=Voice.FEMALE,
          loop=3)

gather.addElement(say)

response = Response()
response.addElement(gather)

print(response.xml)
