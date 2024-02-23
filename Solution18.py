validString = lambda value: (any(char.isupper() for char in value)
                             and any(char.islower() for char in value)
                             and any(char.isdigit() for char in value)
                             and len(value) >= 10)

result = validString("PaceWisd0m o/p")
print(result)
