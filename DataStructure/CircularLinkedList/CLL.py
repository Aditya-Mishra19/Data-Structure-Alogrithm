import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class LinkedList: 

    def __init__(self): 
        self.head = None


    def display(self):
        temp = self.head 
        while (temp.next is not self.head): 
            print(temp.info)
            temp = temp.next
        print(temp.info)
    def insert_at_beg(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            self.head.next=self.head
            return
        self.p=self.head
        while self.p.next is not self.head:
            self.p=self.p.next
        self.temp.next=self.head
        self.p.next=self.temp
        self.head=self.temp
    def insert_at_end(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            self.head.next=self.head
            return
        self.p=self.head
        while self.p.next is not self.head:
            self.p=self.p.next
        self.p.next=self.temp
        self.temp.next=self.head
    def insert_after_given_node(self,data,item):
        self.p=self.head
        while self.p.next is not self.head:
            if self.p.info==item:
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        if self.p.info==item:
            self.temp=node(data)
            self.p.next=self.temp
            self.temp.next=self.head
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next==self.head:
            if self.head.info==data:
                self.temp=self.head;
                self.head=None
                return
            
            else:
                print("element not found")
                return
        
        if self.head.next.info==data:
            self.temp=self.head.next
            self.head.next=self.temp.next
            return
        self.p=self.head.next
        while(self.p.next is not self.head):
            if(self.p.next.info==data): 
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.p.next
        
        if(self.head.info==data):    
            self.temp=self.head
            self.p.next=self.head.next
            self.head=self.p.next
            return
            
        
if __name__=='__main__': 

    llist = LinkedList()
    while(1):
        print("1.Display\n")
        print("2.Insert new node at the beginning\n")
        print("3.Insert new node at the end\n")
        print("4.Insert new node after the given node\n")
        print("5.Delete node\n")
        print("6.Quit\n\n")
        print("Enter your choice : ")
        choice=int(input())
        if(choice==1):
            llist.display()
        elif(choice==2):
            value=int(input())
            llist.insert_at_beg(value)
        elif(choice==3):
            value=int(input())
            llist.insert_at_end(value)
        elif(choice==4):
            print("enter the value")
            value=int(input())
            print("Enter the element after which to insert : ")
            item=int(input())
            llist.insert_after_given_node(value,item)
        elif(choice==5):
            value=int(input())
            llist.delete(value) 
        else:
            sys.exit(0)
        


