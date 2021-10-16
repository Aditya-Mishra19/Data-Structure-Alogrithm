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
        while (temp): 
            print (temp.info) 
            temp = temp.next
    
    def count(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    def serach(self,value):
        temp=self.head
        pos=1
        while(temp):
            if(temp.info==value):
                print("The value found at",pos)
            temp=temp.next
            pos+=1
        print("Value not found in the linked list")
        
    def insert_at_beg(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.temp.next = self.head
        self.head= self.temp
        
    def insert_at_end(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.p = self.head
        while self.p.next is not None:
            self.p=self.p.next
        self.p.next = self.temp;
        
    def insert_after_given_node(self,data,item):
        self.p=self.head
        while self.p is not None:
            if(self.p.info==item):
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        print("Item not found")

    def insert_at_pos(self,data,pos):
        self.temp=node(data)
        if pos==1:
            self.temp.next = self.head
            self.head= self.temp
            return
        self.p=self.head
        while pos>2 and self.p is not None:
            self.p=self.p.next
            pos-=1
        if self.p is None:
            print("Position exceeded the length of the list")
        else:
            self.temp.next=self.p.next
            self.p.next=self.temp
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info==data:
            self.temp=self.head
            self.head=self.head.next
            return
        self.p=None
        self.curr=self.head
        while self.curr is not None:
            if self.curr.info==data:
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.curr
            self.curr=self.curr.next
            
    def reverse(self):
        self.prev=None
        self.curr=self.head
        while self.curr is not None:
            self.Next=self.curr.next
            self.curr.next=self.prev
            self.prev=self.curr
            self.curr=self.Next
        self.head=self.prev
        return


if __name__=='__main__': 

    llist = LinkedList() 

    while(1):
        print("1.Display\n");
        print("2.Count list\n");
        print("3.Search element\n");
        print("4.Insert new node at the beginning\n");
        print("5.Insert new node at the end\n");
        print("6.Insert new node after the given node\n");
        print("7.Insert new node at the given position\n");
        print("8.Delete node\n");
        print("9.Reverse list\n");
        print("10.Quit\n\n");
        print("Enter your choice : ");
        choice=int(input())
        if(choice==1):
            llist.display()
        elif(choice==2):
            llist.count()
        elif(choice==3):
            value=int(input())
            llist.search(value)
        elif(choice==4):
            value=int(input())
            llist.insert_at_beg(value)
        elif(choice==5):
            value=int(input())
            llist.insert_at_end(value)
        elif(choice==6):
            print("enter the value")
            value=int(input())
            print("Enter the element after which to insert : ")
            item=int(input())
            llist.insert_after_given_node(value,item)
        elif(choice==7):
            print("enter the value")
            value=int(input())
            print("Enter the position to insert : ")
            item=int(input())
            llist.insert_at_pos(value,item)
        elif(choice==8):
            value=int(input())
            llist.delete(value) 
        elif(choice==9):
            llist.reverse() 
        else:
            sys.exit(0)
        

