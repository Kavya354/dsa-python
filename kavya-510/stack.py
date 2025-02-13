def PUSH(data):
    if len(stack)<capacity:
        stack.append(data)
        print(data,"is pushed into stack")
    else:
        print("stack overflow")
    
def POP():
    if stack:#len(stack)>0
        print(stack[-1],"popped from stack")
        stack.pop()
    else:
        print("stack overflow")
def PEEK():
    if stack:
        print("is top element of the stack",stack[-1])
    else:
        print("stack is empty")
def Display():
    if stack:
        print(stack)
    else:
        print("stack is empty")
if __name__=="__main__":
    stack=[]

    capacity=int(input("enter stack capacity:-"))
    print("\n*********WELCOME TO STACK OPERARTIONS***********")
    print("enter 1 to PUSh an element into stack")
    print("enter 2 to POP an element from stack")
    print("enter 3 to PEEk into stack")
    print("enter 4 to Display all elements in stack")
    
    while(True):
        ip=int(input("enter your choice:-"))
        if ip==1:
            data=int(input("enter your push value:-"))
            PUSH(data)
        elif ip==2:
             POP()
        elif ip==3:
            PEEK()
        elif ip==4:
            Display()
        elif ip==-1:
            print("you have exited the program")
            break
        else:
            print("Invalid choice")


    

                    
        