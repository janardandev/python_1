#Lambda
from functools import reduce

s=lambda x:x**2
print(s(10))
s=lambda x,y:x*y
print(s(2,7))
s=lambda x,y,z:x*y*z
print(s(2,7,4))
s=lambda a,b,c:a if a>b and b>c else b if b>c else c
print(s(2,5,3))
#Filter
s=filter(lambda x:x%2==0,[1,2,3,4,5,6])
for x in s:
    print(x)
l=[1,2,3,4,5,6]
s=list(filter(lambda x:x%2==0,l))
print(s)
#Map
l1=[1,2,3]
l2=[2,3,4]
s=map(lambda x,y:x*y,l1,l2)
for a in s:
    print(a)

l1=[1,2,3]
l2=[2,3,4]
s=list(map(lambda x,y:x*y,l1,l2))
print(s)
l3=[2,2,2]
s=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(s)

#Reduce
s=reduce(lambda x,y:x*y,[8,2,3])
print(s)