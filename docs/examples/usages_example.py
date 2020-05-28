from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from zang.domain.enums.product import Product

from docs.examples.credentials import sid, authToken
url = 'http://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
usagesConnector = ConnectorFactory(configuration).usagesConnector


# view usage
try:
    usage = usagesConnector.viewUsage('{UsageSid}')
    print(usage.totalCost)
except ZangException as ze:
    print(ze)


# list usages
try:
    product = Product.ordinal(Product.OUTBOUND_CALL)
    usages = usagesConnector.listUsages(
        product=product,
        year=2017,
        month=2,
        pageSize=100)
    if usages and usages.elements:
        total = 0.0
        for usage in usages.elements:
            total += usage.totalCost
        print(total)
except ZangException as ze:
    print(ze)
