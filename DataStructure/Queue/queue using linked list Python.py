import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class Queue: 

    def __init__(self): 
        self.front = None
        self.rear = None
        
    
    def isEmpty(self):
        if self.front is None:
            return True
        return False
    
    def insert(self,data):
        self.temp=node(data)
        if self.temp is None:
            print("No memory")
            return
        if self.front is None:
            self.front=self.temp
        else:
            self.rear.next=self.temp
        self.rear= self.temp
    
    def delete(self):
        if self.isEmpty():
            print("Queue Underflow")
            sys.exit(0)
        d=self.front.info
        self.front=self.front.next    
        return d
    
    def peek(self):
        if self.isEmpty():
            print("Queue Underflow")
            sys.exit(0)
        d=self.front.info
        return d
    def display(self):
        if self.isEmpty():
            print("Queue Underflow")
            sys.exit(0)
        self.p=self.front
        while self.p is not None:
            print(self.p.info)
            self.p=self.p.next
            
    
        
if __name__=='__main__': 

    q = Queue()
    while(1):
        print("1.Push\n");
        print("2.Pop\n");
        print("3.Display the top element\n");
        print("4.Display all stack elements\n");
        print("5.Quit\n");
        print("Enter your choice : ");
        choice=int(input())
        if choice==1:
            value=int(input())
            q.insert(value)
        elif choice==2:
            d=q.delete()
            print("poped value",d)
        elif choice==3:
            print("top of the element",q.peek())
        elif choice==4:
            q.display()
        else:
            sys.exit(0)
            
            
        

