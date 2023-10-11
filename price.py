import requests
import json
from balanceUpdates import min_time, max_time
url = "https://streaming.bitquery.io/graphql"
import pandas as pd

payload = json.dumps({
   "query": "query MyQuery {\n  EVM(dataset: combined, network: eth) {\n    latest: DEXTrades(\n      where: {Trade: {Buy: {Currency: {SmartContract: {is: \"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48\"}}}}}\n      limit: {count: 1}\n      orderBy: {descending: Block_Time}\n    ) {\n      Block {\n        Time\n      }\n      Trade {\n        Buy {\n          Price\n        }\n      }\n    }\n    min_trade: DEXTrades(\n      where: {Trade: {Buy: {Currency: {SmartContract: {is: \"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48\"}}}}, Block: {Time: {after:\"" +min_time+ "\"}}}\n       limit: {count: 1}\n      orderBy: {ascending: Block_Time}\n    ) {\n      Block {\n        Time\n      }\n      Trade {\n        Buy {\n          Price\n        }\n      }\n    }\n  }\n}\n",
   "variables": "{}"
})
headers = {
   'Content-Type': 'application/json',
   'X-API-KEY': 'keyy'
}

response = requests.request("POST", url, headers=headers, data=payload)
# Parse the JSON response
response_json = json.loads(response.text)

# Extract the data you need (price values)
latest_prices = response_json['data']['EVM']['latest']

earliest_prices = response_json['data']['EVM']['min_trade']


trade_latest = pd.DataFrame(latest_prices, columns=[ 'Block', 'Trade'])

trade_earliest = pd.DataFrame(earliest_prices, columns=[ 'Block', 'Trade'])

print(trade_latest)
print(trade_earliest)
