# Using While loop


def Calculate_While(a):
    size = len(a)
    size1 = size - 1
    c = []
    j = 0

    while j < size:
        c.append(a[j] + a[size1])
        j = j + 1
        size1 = size1 - 1

    print("The Output is = ", c)

# Using reverse() built in function


def Calculate_Reverse(a):
    e = list(a)
    e.reverse()
    size = len(e)
    c = list()
    while size != 0:
        c.append(a.pop() + e.pop())
        size = size - 1
    print("The Output is = ", c)

# Using For loop


def Calculate_For(a):
    size = len(a)
    size1 = size - 1
    c = []

    for x in a:
        c.append(x+a[size1])
        size1 = size1 - 1

    print("The Output is = ", c)


iValue = 1

while iValue != 0:

    print("----------------------------------------------------")
    print("1 : Perform Operation Using While Loop")
    print("2 : Perform Operation Using In-built function reverse")
    print("3 : Perform Operation Using For Loop")
    print("4 : Exit From The Application")
    print("-----------------------------------------------------")
    iChoice = int(input("Enter The Choice: -"))

    if iChoice == 1:
        length = int(input("Enter the size of array = "))
        b = list()
        i = 0

        while i < length:
            ele = int(input("Enter the element in the array = "))
            b.insert(i, ele)
            i = i + 1
        Calculate_While(b)
    elif iChoice == 2:
        length = int(input("Enter the size of array = "))
        b = list()
        i = 0

        while i < length:
            ele = int(input("Enter the element in the array = "))
            b.insert(i, ele)
            i = i + 1
        Calculate_Reverse(b)
    elif iChoice == 3:
        length = int(input("Enter the size of array = "))
        b = list()
        i = 0

        while i < length:
            ele = int(input("Enter the element in the array = "))
            b.insert(i, ele)
            i = i + 1
        Calculate_For(b)
    elif iChoice == 4:
        print("Thank You For Using Our Application !")
        iValue = 0
        break
    else:
        print("Invalid Choice Has Been Entered !")
