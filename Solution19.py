checkSubString = lambda listValue, subValue: subValue in listValue

values = ['red', 'black', 'white', 'green', 'orange']
subValue = "xy"
found = False

for val in values:
    if checkSubString(val, subValue):
        print("Elements of the said list that contain specific substring: ['", val, "']")
        found = True
        break

if found:
    pass
else:
    print("Elements of the said list that contain specific substring: []")