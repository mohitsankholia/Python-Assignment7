class ReverseString:
    def reverseString(self):
        global inputString
        inputString = input("Enter String to reverse : ")
        words = inputString.split()
        print(words)
        outputString = ' '.join(reversed(words))
        return outputString


stringReverse = ReverseString()
resultString = stringReverse.reverseString()
print("output string :", resultString)
