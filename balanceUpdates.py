import requests
import json

url = "https://streaming.bitquery.io/graphql"

payload = json.dumps({
   "query": "query MyQuery {\n  EVM(dataset: combined, network: eth) {\n    BalanceUpdates(\n      where: {BalanceUpdate: {Address: {is: \"0x3416cf6c708da44db2624d63ea0aaef7113527c6\"}}, Currency: {SmartContract: {is: \"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48\"}}}\n      orderBy: {ascending: Block_Time}\n      limit: {count: 10}\n    ) {\n      Currency {\n        Name\n        SmartContract\n      }\n      balance: sum(of: BalanceUpdate_Amount, selectWhere: {gt: \"0\"})\n      Block {\n        Time\n      }\n    }\n  }\n}\n",
   "variables": "{}"
})
headers = {
   'Content-Type': 'application/json',
   'X-API-KEY': 'keyy'
}

response = requests.request("POST", url, headers=headers, data=payload)


import pandas as pd

# Parse the JSON response
response_json = json.loads(response.text)

# Extract the balance updates data
balance_updates = response_json['data']['EVM']['BalanceUpdates']

# Create a dataframe from the balance updates data
df = pd.DataFrame(balance_updates, columns=['Currency', 'Block', 'BalanceUpdate','balance'])


# Extract the Time column from the Block array
block_times = df['Block'].apply(lambda x: x['Time'])

Balances=df['balance']

# Combine the two DataFrames into a new DataFrame
combined_df = pd.concat([block_times, Balances], axis=1)

# Rename the columns for clarity
combined_df.columns = ['Block_Time', 'Balance']


# Find the minimum and maximum values of the Time column
min_time = block_times.min()
max_time = block_times.max()



