sortTuple = lambda enteredValue: sorted(enteredValue, key=lambda x: x[1])

values = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

result = sortTuple(values)
print(result)
