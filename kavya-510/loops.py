#for loop
n=5
for i in range(1,n):
    print(i,end=" ")
#odd
n=10
for i in range(1,n):
    if(i%2!=0):
      print(i)
#odd
n=10
for i in range(1,n,2):
  print(i)
#even 
n=10
for i in range(2,n,2):
    print(i)
#reverse
n=10
for i in range(n,0,-1):
    print(i)
#reverse of odd 
n=10
for i in range(n,0,-1):
     if(i%2!=0):
        print(i)
