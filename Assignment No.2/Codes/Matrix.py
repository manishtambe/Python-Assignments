
def CreateMatrix():

    row = int(input("Enter the number of rows to create an 1st matrix = "))
    col = int(input("Enter the number of cols to create an 1nd matrix = "))

    if row == col:

        a = [[0 for x in range(row)] for y in range(col)]

        for i in range(0, row):
            for j in range(0, col):
                element = int(input("Enter The Element of 1st matrix= "))
                a[i][j] = element

        row1 = int(input("Enter the number of rows to create an 2nd matrix = "))
        col1 = int(input("Enter the number of cols to create an 2nd matrix = "))
        if (row + col) == (row1 + col1):
            if row1 == col1:
                b = [[0 for x in range(row1)] for y in range(col1)]
                for i in range(0, row1):
                    for j in range(0, col1):
                        element = int(input("Enter The Element of 2nd matrix= "))
                        b[i][j] = element
                Menu(row1, col1, a, b)
            else:
                print("Matrix should have same number of Rows and columns!")
        else:
            print("Please enter both the matrix of equal size !")
    else:
        print("Matrix should have same number of Rows and columns!")


def DisplayMatrx(row, col, a, b):
    print("Elements From First matrix = ")
    for i in range(0, row):
        print(a[i])
    print("Elements From Second matrix = ")
    for i in range(0, row):
        print(b[i])


def Addition(row, col, a, b):

    c = [[0 for x in range(row)] for y in range(col)]

    for x in range(0, row):
        for y in range(0, col):
            c[x][y] = a[x][y] + b[x][y]

    print("The addition of the both the matrix = ")
    for x in range(0, row):
        print(c[x])
    Transpose(row, col, c)


def Subtraction(row, col, a, b):

    c = [[0 for x in range(row)] for y in range(col)]

    for x in range(0, row):
        for y in range(0, col):
            c[x][y] = a[x][y] - b[x][y]

    print("The subtraction of the both the matrix = ")
    for x in range(0, row):
        print(c[x])
    Transpose(row, col, c)


def Multiplication(row, col, a, b):
    c = [[0 for x in range(row)] for y in range(col)]
    k = 0
    for x in range(0, row):
        for y in range(0, col):
            for k in range(0, col):
                c[x][y] += (a[x][k] * b[k][y])
    print("The multiplication of the both the matrix = ")
    for x in range(0, row):
        print(c[x])
    Transpose(row, col, c)


def Transpose(row, col, c):
    d = [[0 for x in range(row)] for y in range(col)]

    for x in range(0, row):
        for y in range(0, col):
            d[x][y] = c[y][x]

    print("The Transpose of the output matrix is: -")
    for x in range(0, row):
        print(d[x])
    ans = Symmetric(row, col, d, c)
    print("is matrix is symmetric matrix? = ", ans)
    ans = BinaryMatrix(row, col, c)
    print("is matrix is binary matrix? = ", ans)


def Symmetric(row, col, d, c):
    flag = 0
    for x in range(0, row):
        for y in range(0, col):
            if d[x][y] != c[x][y]:
                flag = 1
    if flag == 0:
        return True
    else:
        return False


def BinaryMatrix(row, col, c):
    flag = 0
    for x in range(0, row):
        for y in range(0, col):
            if c[x][y] != 1:
                if c[x][y] != 0:
                    flag = 1
    if flag == 0:
        return True
    else:
        return False


def Menu(row, col, a, b):
    value = 1

    while value != 0:
        print("------------------------------------------")
        print("1: Display Both The Matrix")
        print("2: Matrix Addition")
        print("3: Matrix Subtraction")
        print("4: Matrix Multiplication")
        print("5: Exit From The Application")
        print("------------------------------------------")
        choice = int(input("Enter the choice = "))

        if choice == 1:
            DisplayMatrx(row, col, a, b)
        elif choice == 2:
            print("1: Matrix Addition = ")
            Addition(row, col, a, b)
        elif choice == 3:
            print("2: Matrix Subtraction = ")
            Subtraction(row, col, a, b)
        elif choice == 4:
            print("4: Matrix Multiplication = ")
            Multiplication(row, col, a, b)
        elif choice == 5:
            print("Thank You For Using Application !")
            value = 0
        else:
            print("Invalid Choice Has Been Entered !")


CreateMatrix()
