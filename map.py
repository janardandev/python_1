l=[1,2,3,4,5]
out=list(map(lambda x:x**2,l))
print(out)

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
out=list(map(lambda x,y:x*y,l1,l2))
print(out)

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
l3=[1,2,3,4,5]
out=list(map(lambda x,y,z:x*y*z,l1,l2,l3))
print(out)

l=[1,2,3,4,5]
out=list(map(lambda x:x%3==0,l))
print(out)