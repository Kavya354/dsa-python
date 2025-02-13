class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    capacity=5
    top=0
    def __init__(self):
        self.Head=None
def PUSH(self,data):
        newnode=Node(data)
    if self.top<self.capacity:
        print(newnode.data,"is pushed into stack")
        newnode.next=newnode
        self.top +=1
    else:
        print("stack overflow")
def POP(self):
    if self.top>0:
            print(self.Head.data,"is popped from stack")
            self.Head=self.Head.next
            self.top-=1
    else:
          print("stack underflow")

def PEEk(self):
    if self.top>0:
            print(self.Head.data,"is top element in stack")
    else:
          print("stack is empty")
def Display(self):
    if self.top<=0:
            print("stack is empty")
    else:
          print("stack:-",end='')
          temp=self.Head
          while temp:
                print(temp)
            
    
    

             
def Display(self):
        temp=self.Head
        while(temp!=None):
            print(hash(temp),temp.data,hash(temp.next))
        temp=temp.next
if __name__=="__main__": 
    capacity=int(input("enter stack capacity:-"))
stk=Stack()
stk.PUSH(1)
stk.PUSH(3)
stk.Display()