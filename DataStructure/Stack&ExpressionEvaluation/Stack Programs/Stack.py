class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
    
    def Push(self, ele):
        self.stack.append(ele)
    
    def Pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    
    def peek (self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1
    
    def display (self):
        print("Element present in Stack")
        for i in self.stack:
            print(i, end= " ")

s = Stack() # instance
while True:
    print("\nChoose the operation\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exist")
    do = int(input("Enter your choice: "))

    if do == 1:
        ele = int(input("Enter the element you want to insert into stack: "))
        s.Push(ele)

    elif do == 2:
        ele = s.Pop()
        if ele == -1:
            print("Stack Underflow")
        else:
            print("{} element is deleted from the stack".format(ele))
    
    elif do == 3:
        ele = s.peek()
        if ele == -1:
            print("Stack Underflow")
        else:
            print("{} element is on the top of the stack".format(ele))

    elif do == 4:
        s.display()
    
    elif do == 5:
        break


    