def Function():
    print(a)#not local variable

if __name__=="__main__":
    a=5
    Function()
    print(a)
