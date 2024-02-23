checkDivisible = lambda number: number % 13 == 0 or number % 19 == 0

values = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
newList = []

for val in values:
    if checkDivisible(val):
        newList.append(val)

print(newList)