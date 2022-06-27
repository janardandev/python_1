from functools import reduce

s=lambda a,b:a+b
print(s(10,20))

s=lambda x:x*x
print(s(10))

s=lambda x,y,z:(x+y+z)**3
print(s(1,2,3))

s=lambda x,y:x+y
print(s(10,40))
l=[12,3,4,5,6,7,87,9]
s3=list(filter(lambda x,y:(x+y)**2),l)
print(s3())

l=[12,3,4,5,6,7,87,9]
l1=list(filter (lambda x:x%2==0,l) )
print(l1)