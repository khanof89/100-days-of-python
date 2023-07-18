print('Welcome to tip calculator.')
bill = int(input('What was the total bill?'))
people = int(input('How many people to split the bill'))
tip = int(input('What percentage tip would you like to give?'))
amount_to_pay = (bill+(bill * tip /100)) / people
print('Each person should pay: $', amount_to_pay)