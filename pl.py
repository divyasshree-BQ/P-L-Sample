# Calculate P&L Formula
#change_in_balance = final_balance - initial_balance
# change_in_price = final_price - initial_price
# pnl = change_in_balance * change_in_price

from balanceUpdates import combined_df,Balances

from price import trade_latest, trade_earliest
initial_balance=Balances[0]
final_balance = Balances.tail(1).values[0] 

initial_price=trade_earliest['Trade'][0]['Buy']['Price']
final_price=trade_latest['Trade'][0]['Buy']['Price']

# Convert the string values to floats
initial_balance = float(initial_balance)
final_balance = float(final_balance)
initial_price = float(initial_price)
final_price = float(final_price)

# Calculate P&L
change_in_balance = final_balance - initial_balance
change_in_price = final_price - initial_price
pnl = change_in_balance * change_in_price

print("Profit",pnl)