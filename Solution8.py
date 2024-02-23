class ReverseString:

    def __init__(self):
        self.inputString = ""

    def getString(self):
        self.inputString = input("Enter a string to reverse: ")

    def reverseString(self):
        reversed_string = self.inputString[::-1]
        print("Reversed String:", reversed_string)


outputString = ReverseString()
outputString.getString()
outputString.reverseString()