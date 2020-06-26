# this is a (very) simple Dollars to Cents converter


print("Simply enter in your amount in dollars and we will tell you your change!!")

dollar_amount = float(input('Enter how much money you have in dollars: '))
cents = dollar_amount * 100

quarters, qRemainder = divmod(cents, 25)
dimes, dRemainder = divmod(qRemainder, 10)
nickles, nRemainder = divmod(dRemainder, 5)
pennies, pRemainder = divmod(nRemainder, 1)

print('')
print(f"If you have {dollar_amount}$ then you have Quarters: {int(quarters)}, Dimes: {int(dimes)}, "
      f"Nickles: {int(nickles)}, and Pennies: {int(pennies)}!")

