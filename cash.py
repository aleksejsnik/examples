# A code that first asks the user how much change is owed
# and then prints the minimum number of coins
# with which that change can be made.

from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break


#count of quaters
quarters = change / 0.25
change = change % 0.25
quarters = int(quarters)

#count of dimes
dimes = change / 0.1
change = change % 0.1
dimes = int(dimes)

#count of nickels
nickels = change / 0.05
change = change % 0.05
nickels = int(nickels)

#count of pennies
pennies = change / 0.01
pennis = int(pennies)

#total coins
coins = quarters + dimes + nickels + pennies
print(int(round(coins, 0)))
