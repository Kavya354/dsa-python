class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.Head=None
        self.Tail=None
    
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
            self.Tail=newnode
        else:
            newnode.prev=self.Tail
            self.Tail.next=newnode
            self.Tail=newnode
    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
            self.Tail=newnode
        else:
            newnode.next=self.Head
            self.Head.prev=newnode
            self.Head=newnode
    def InsertAtPosition(self,data,pos):
        newnode = Node(data)
        temp = self.Head
        while(pos-1 != 0):
            temp = temp.next 
            pos = pos-1
        
        newnode.prev= temp
        newnode.next=temp.next
        temp.next = newnode
        newnode.next.prev=newnode
    def DeleteAtEnd(self):
        if self.Head == None:
            print("List is Empty")
        elif self.Head.next == None:
            self.Head = None
            self.Tail=None
        else:
            self.Tail=self.Tail.prev
            self.Tail.next=None
    def DeleteAtBegin(self):
        self.Head = self.Head.next
        self.Head.prev=None
    def DeleteAtPosition(self,pos):
        if pos==1:
            self.Head = self.Head.next
            self.Head.prev=None
        else:
            temp=self.Head
            while(pos-2!=0):
                temp=temp.next
                pos=pos-1
            temp.next=temp.next.next
            temp.next.prev=temp
      
    def Display(self):
        temp = self.Head 
        while(temp!=None):
            print(hash(temp.prev),hash(temp),temp.data,hash(temp.next))
            temp = temp.next 
    def DisplayReverse(self):
        temp = self.Tail
        while(temp!=None):
            print(hash(temp.prev),hash(temp),temp.data,hash(temp.next))
            temp = temp.prev
            
dll=DoublyLinkedList()
dll.InsertAtEnd(1)
dll.InsertAtEnd(2)
dll.InsertAtEnd(3)
dll.Display();print()
dll.InsertAtBegin(0)
dll.Display();print()
dll.InsertAtPosition(4,2)
dll.Display();print()
dll.DeleteAtEnd()
dll.Display();print()
dll.DeleteAtBegin()
dll.Display();print()
dll.DeleteAtPosition(2)
dll.Display()
    

    

