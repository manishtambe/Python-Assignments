class Student:
    id = 0
    name = ""
    age = 0
    m1, m2, m3 = 0, 0, 0
    total = 0
    percentage = 0.0
    status = ""
    grade = ""

    def AcceptInput(self):
        while True:
            try:
                self.id = int(input("Enter the id of the student = "))
                if self.id <= 0:
                    print("Please enter valid student id")
                else:
                    break
            except:
                print("Please enter valid student id")
                continue

        while True:
            try:
                self.age = int(input("Enter The Age Of The Student = "))
                if self.age <= 0 or self.age >= 60:
                    print("Please enter valid student age")
                else:
                    break
            except:
                print("Please enter valid student age")
                continue

        while True:
            try:
                self.name = input("Enter The name Of The Student = ")
                if len(self.name) <= 2:
                    print("Please enter valid student name")
                else:
                    if self.name.replace(" ", "").isalpha():
                         break
                    else:
                        print("Please enter valid student name")
                        continue
            except:
                print("Please enter valid student name")
                continue

        while True:
            try:
                self.m1 = int(input("Enter The Student Marks In Maths Subject Out Of 100= "))
                if self.m1 <= 0 or self.m1 >= 100:
                    print("Please enter valid student marks")
                else:
                    break
            except:
                print("Please enter valid student marks")
                continue


        while True:
            try:
                self.m2 = int(input("Enter The Student Marks In Science Subject Out Of 100= "))
                if self.m2 <= 0 or self.m2 >= 100:
                    print("Please enter valid student marks")
                else:
                    break
            except:
                print("Please enter valid student marks")
                continue

        while True:
            try:
                self.m3 = int(input("Enter The Student Marks In English Subject Out Of 100= "))
                if self.m3 <= 0 or self.m3 >= 100:
                    print("Please enter valid student marks")
                else:
                    break
            except:
                print("Please enter valid student marks")
                continue


    def Calculate(self):
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = ((self.total * 100) / 300)

        if self.percentage >= 75:
            self.grade = "A"
            self.status = "Pass"
        elif 60 <= self.percentage < 75:
            self.grade = "B"
            self.status = "Pass"
        elif 50 <= self.percentage < 60:
            self.grade = "C"
            self.status = "Pass"
        else:
            self.grade = "No Grade"
            self.status = "Fail"

        print("Student Id: ", self.id)
        print("Student Name: ", self.name)
        print("Student Age: ", self.age)
        print("Student Marks In Maths = ", self.m1)
        print("Student Marks In Science = ", self.m2)
        print("Student Marks In English = ", self.m3)
        print("Student Total Marks = ", self.total)
        print("Student Percentage = ", self.percentage)
        print("Student Status = ", self.status)
        print("Student Grade = ", self.grade)


Obj = Student()
Obj.AcceptInput()
Obj.Calculate()
