#
# This is a common set of reusable python functions
#

from polygon import RESTClient

client = RESTClient("Lmxh45Sd1XptLOy_KKAATu9nE2oQ_5tp")

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "minute",
    "2022-01-01",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)

