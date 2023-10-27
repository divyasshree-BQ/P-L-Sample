import requests
import json
from balanceUpdates import min_time, max_time
url = "https://streaming.bitquery.io/graphql"
import pandas as pd


payload = json.dumps({
   "query": "query MyQuery {\n  EVM(dataset: combined, network: eth) {\n    min_trade: DEXTradeByTokens(\n      where: {Trade: {Currency: {SmartContract: {is: \"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48\"}}}, Block: {Date: {after: \"" +min_time+ "\"}}}\n      limitBy: {by: Block_Date, count: 1}\n      orderBy: {ascending: Block_Date}\n      limit: {count: 1}\n    ) {\n      Block {\n        Date\n      }\n      Trade {\n        Price\n      }\n    }\n    latest: DEXTradeByTokens(\n      where: {Trade: {Currency: {SmartContract: {is: \"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48\"}}}, Block: {Date: {is: \"" +max_time+ "\"}}}\n      limitBy: {by: Block_Date, count: 1}\n   orderBy: {ascending: Block_Date}\n     limit: {count: 1}\n    ) {\n      Block {\n        Date\n      }\n      Trade {\n        Price\n      }\n    }\n  }\n}\n",
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
print("latest_prices",latest_prices)
earliest_prices = response_json['data']['EVM']['min_trade']
print("earliest_prices",earliest_prices)

trade_latest = pd.DataFrame(latest_prices, columns=[ 'Block', 'Trade'])

trade_earliest = pd.DataFrame(earliest_prices, columns=[ 'Block', 'Trade'])

print(trade_latest)
print(trade_earliest)
