def Function():
    a=5#local to scope(Function)
    print(a)
if __name__=="__main__":
    a=6#local bvariable
    print(a)
    Function()
    print(a)
    
