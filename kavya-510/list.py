l=[]
print(l)
l=[1,2,3,4]
print(l)
l=[1.4,2.5]
print(l)
l=['apple']
print(l)
l=['apple',1,2.4]
print(l)

#printing values
l=[10,20,20]
for i in range(0,len(l)):
     print(l[i],end=' ')

print()
for i in l:
    print(i,end=' ')

#list input
l=list(map(int,input().split()))
print(l)

#basics fun
l=[1,2,3,4,5]
print(len(l))
print(sum(l))
print(max(l))
print(min(l))

#fun
l=[1,2,3]
print(l)

l.append(4)
print(l)

l.extend([5,6,7])
print(l)

l.insert(4,8)
print(l)

l.pop()
print(l)

l.remove(2)
print(l)

l.clear()
print(l)
 
