fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')


# For Loop with Range
for number in range(1, 10): # No se incluye el ultimo numero del rango
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)