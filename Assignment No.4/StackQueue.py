class Stack:
    def __init__(self, no):
        self.no = no
        self.l1 = list()

    def push(self, ino):

        if len(self.l1) == self.no:
            print("Stack is full !")
            return
        else:
            self.l1.append(ino)
            print("Element pushed successfully !")

    def pop(self):

        if len(self.l1) == 0:
            print("Stack is empty !")
        else:
            print("The popped element is: -", self.l1.pop())

    def Display(self):
        print("The elements from the stack: -", self.l1)


class Queue:
    def __init__(self, no):
        self.no = no
        self.l1 = list()

    def enqueue(self, ino):
        if len(self.l1) == self.no:
            print("Queue is full !")
        else:
            self.l1.append(ino)
            print("Element added in queue successfully")

    def dequeue(self):
        if len(self.l1) == 0:
            print("The queue is empty !")
        else:
            print("The deleted element is: -", self.l1.pop(0))

    def Display(self):
        print("The elements from the queue: -", self.l1)


Value = 1
Value1 = 1
Value2 = 1
while Value != 0:
    print("|-----------------------------|")
    print("|-------Stack And Queue-------|")
    print("|-----------------------------|")
    print("|-----------1.Stack-----------|")
    print("|-----------2.Queue-----------|")
    print("|-----------3.Exit------------|")
    print("|-----------------------------|")
    iChoice = int(input("Enter The Choice: -"))
    if iChoice == 1:
        size = int(input("Enter the size of the stack: -"))
        Obj = Stack(size)
        while Value1 != 0:
            print("|----------------------------------|")
            print("|---------Stack Operations---------|")
            print("|----------------------------------|")
            print("|-----1 : Push element in stack----|")
            print("|-----2 : Pop element in stack-----|")
            print("|3 : Display element from the stack|")
            print("|-----4 : Exit From Application----|")
            print("|----------------------------------|")
            iChoice = int(input("Enter The Choice: -"))
            if iChoice == 1:
                ele = int(input("Enter the value that you want to insert in the stack: -"))
                Obj.push(ele)
            elif iChoice == 2:
                Obj.pop()
            elif iChoice == 3:
                Obj.Display()
            elif iChoice == 4:
                Value1 = 0
                print("Thank You For Using Application")
                break
            else:
                print("Undefined choice has been entered !")
    elif iChoice == 2:
        size = int(input("Enter the size of the Queue: -"))
        Obj1 = Queue(size)
        while Value2 != 0:
            print("|----------------------------------|")
            print("|---------Queue Operations---------|")
            print("|----------------------------------|")
            print("|-----1 : Push element in Queue----|")
            print("|-----2 : Pop element in Queue-----|")
            print("|3 : Display element from the Queue|")
            print("|-----4 : Exit From Application----|")
            print("|----------------------------------|")
            iChoice = int(input("Enter The Choice: -"))
            if iChoice == 1:
                ele = int(input("Enter the value that you want to insert in the queue: -"))
                Obj1.enqueue(ele)
            elif iChoice == 2:
                Obj1.dequeue()
            elif iChoice == 3:
                Obj1.Display()
            elif iChoice == 4:
                Value2 = 0
                print("Thank You For Using Application")
                break
            else:
                print("Undefined choice has been entered !")
    elif iChoice == 3:
        iValue = 0
        print("Thank you for using application")
        break
    else:
        print("Undefined choice has been entered !")
