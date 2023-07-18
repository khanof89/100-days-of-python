import math
print('Welcome to tip calculator.')
bill = float(input('What was the total bill?'))
people = float(input('How many people to split the bill'))
tip = float(input('What percentage tip would you like to give?'))
amount_to_pay = (bill+(bill * tip /100)) / people
print('Each person should pay: $', math.ceil(amount_to_pay))