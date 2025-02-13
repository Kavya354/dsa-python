class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.Head=None
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
        else:
            temp=self.Head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
        else:
           newnode.next=self.Head
           self.Head=newnode
    def InsertAtPosition(self,pos,data):
        newnode=Node(data)
        temp=self.Head
        while(pos-1!=0):
            temp=temp.next
            pos-=1
        newnode.next=temp.next
        temp.next=newnode
    def DeleteAtEnd(self):
        if self.Head==None:
            print("List is empty")
        elif self.Head.next==None:
            self.Head=None
        else:
            temp=self.Head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def DeleteAtbeg(self):
        if self.Head==None:
            print("list is empty")
        else:
            self.Head=self.Head.next
   
    def Display(self):
        temp=self.Head
        while(temp!=None):
            print(hash(temp),temp.data,hash(temp.next))
        temp=temp.next

sll=SinglyLinkedList()
sll.InsertAtEnd(1)
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtBegin(0)
sll.InsertAtBegin(-1);print()
sll.Display()
sll.InsertAtPosition(2,5)
sll.Display()
sll.DeleteAtEnd()
sll.Display()
