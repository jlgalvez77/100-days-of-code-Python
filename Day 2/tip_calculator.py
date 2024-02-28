print('Welcome to the tip calculator.')
bill = input('What was the total bill? ')
tip = input('What percentage tip would you like to give? 10, 12 or 15 ')
people = input('How many people to split the bill? ')

bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)

bill_with_tip = (bill_float * tip_int) / 100
total = round((bill_with_tip + bill_float) / people_int, 2)

print(f'Each person should pay: {total}')