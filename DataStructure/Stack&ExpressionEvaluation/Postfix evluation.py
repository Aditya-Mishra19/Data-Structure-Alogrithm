from __future__ import print_function
import sys

class Stack:
    
    def __init__(self):
        self.stack=[None] * 100
        self.top=-1
    def isFull(self):
        if self.top==100:
            return True
        return False
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
        
    def push(self,data):
        if self.isFull():
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=data
        
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        self.top-=1
        return d
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.stack[self.top]
        return d
    
def priority(val):
    if val=='(':
        return 0
    elif val=='+' or val=='-':
        return 1
    elif val=='*' or val=='/' or val=='%':
        return 2
    elif val=='^':
        return 3
    else:
        return 0
    
    
def infixtopostfix(val):
    postfix=[]
    for i in val:
        if i=='(':
            s.push(i)
        elif(i==')'):
            value=s.pop()
            while(value is not '('):
                postfix.append(value)
                value=s.pop()
        elif(i=='+' or i=='-' or i=='*' or i=='/' or i=='%' or i=='^'):
            while((s.isEmpty() is False)and  (priority(s.peek())>= priority(i))):
                postfix.append(s.pop())
            s.push(i)
        else:
            postfix.append(i)
    
    while(s.isEmpty() is not True):
        postfix.append(s.pop())
    return postfix

def postfix_eval(value):
    d=0
    for i in value:
        if i<='9' and i>='0':
            i=int(i)
            s.push(i)
        else:
            a=s.pop()
            b=s.pop()
            if i=='+':
                d=b+a
            elif i=='-':
                d=b-a
            elif i=='*':
                d=b*a
            elif i=='/':
                d=b/a
            elif i=='%':
                d=b%a
            elif i=='^':
                d= b ** a
            s.push(d)
    result=s.pop()
    return result
    
s=Stack()
if __name__=="__main__":
    print("enter the infix expresion")
    infix_val=input()
    postfix=infixtopostfix(infix_val)
    print("postfix expression:",end='')
    for i in postfix:
        print(i,end="")
    print("\n")
    print("postfix evaluation")
    val=postfix_eval(postfix)
    print(val)
    
