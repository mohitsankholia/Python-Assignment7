class CalculatePower:

    def __init__(self):
        pass

    def powerCal(self):

        global multiply
        value = int(input("Enter value : "))
        power = int(input("Enter power : "))

        if power != 1:
            multiply = value * value
            for i in range(3, power + 1):
                multiply = multiply * value

            return multiply

        else:
            return value


obj = CalculatePower()
print("Result : ", obj.powerCal())