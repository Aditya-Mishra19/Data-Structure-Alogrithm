import sys
class Queue:
    
    def __init__(self):
        self.queue=[None] * 100
        self.front=-1
        self.rear=-1
    def isFull(self):
        if (self.rear==100 and self.front==0) and self.front==self.rear+1:
            return True
        return False
    
    def isEmpty(self):
        if self.front==-1:
            return True
        return False
        
    def insert(self,data):
        if self.isFull():
            print("stack overflow")
            return
        if self.front==-1:
            self.front=0
        if self.rear==100:
            self.rear
        else:
            self.rear=self.rear+1
            self.queue[self.rear]=data
            
    def delete(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        elif self.front==100:
            self.front=0;
        else:
            self.front=self.front+1;
        return item
    
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.queue[self.front]
        return d
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        self.temp=self.front
        if self.front<self.rear:
            while self.temp<=self.rear:
                print (self.queue[self.temp])
                self.temp+=1
        else:
            while self.temp<100:
                print(self.queue[self.temp])
                self.temp+=1
            self.temp=0
            while self.temp<=self.rear:
                print(self.queue[self.temp])
                self.temp+=1
                
if __name__=='__main__':
    
    s=Queue()
    while(1):
        print("1.Insert\n");
        print("2.delete\n");
        print("3.Display the top element\n");
        print("4.Display all elements\n");
        print("5.Quit\n");
        print("Enter your choice : ");
        choice=int(input())
        if choice==1:
            value=int(input())
            s.insert(value)
        elif choice==2:
            d=s.delete()
            print("deleted value",d)
        elif choice==3:
            print("top of the element",s.peek())
        elif choice==4:
            s.display()
        else:
            sys.exit(0)
            
            

