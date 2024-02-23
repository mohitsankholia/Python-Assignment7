sortNumberString = lambda value: sorted(value, key=lambda x: (isinstance(x, str), x))

values = [19, 'red', 12, 'green', 'blue', 1, 'white', 'green', 10]

result = sortNumberString(values)
print(result)
