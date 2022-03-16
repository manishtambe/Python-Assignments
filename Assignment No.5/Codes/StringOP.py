class StringOp:
    def __init__(self, input_string):
        self.string = input_string

    def StringtoLower(self):
        temp_str = self.string.lower()
        return temp_str

    def StringtoUpper(self):
        temp_str = self.string.upper()
        return temp_str

    def StringtoCapitalal(self):
        temp_str = self.string.capitalize()
        return temp_str

    def StringtoTitle(self):
        temp_str = self.string.title()
        return temp_str

    def StringCount(self, cnt):
        temp_str = self.string.count(cnt)
        return temp_str


string = str(input("Enter the string to perform operation: - "))
obj = StringOp(string)
iValue = 1
while iValue != 0:
    print("|-----------------------------------------------|")
    print("|----------------String Operation---------------|")
    print("|-----------------------------------------------|")
    print("| 1: Convert string to lower case               |")
    print("| 2: Convert string to upper case               |")
    print("| 3: Convert string to title case               |")
    print("| 4: Convert string to capitalize case          |")
    print("| 5: Count occurrence of letter from string     |")
    print("| 6: Exit from application                      |")
    print("|-----------------------------------------------|")
    iChoice = int(input("Enter the choice: - "))
    if iChoice == 1:
        temp = obj.StringtoLower()
        print("Enter string in lower case form: -", temp)
    elif iChoice == 2:
        temp = obj.StringtoUpper()
        print("Enter string in upper case form: -", temp)
    elif iChoice == 3:
        temp = obj.StringtoUpper()
        print("Enter string in title case form: -", temp)
    elif iChoice == 4:
        temp = obj.StringtoUpper()
        print("Enter string in capitalize case form: -", temp)
    elif iChoice == 5:
        ele = input("Enter the letter of which you want to count Occurrence: -")
        temp = obj.StringCount(ele)
        print("The occurrence of the latter", ele, "is =", temp)
    elif iChoice == 6:
        print("Thank You For Using Application !")
        iValue = 0
        break
    else:
        print("Undefined choice has been entered")
