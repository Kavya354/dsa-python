n=int(input())
if n<0:
    n=n*-1
sum=0
while(n!=0):
        sum+=n%10
        n=n//10
print(sum)



