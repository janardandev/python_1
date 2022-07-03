l=[1,2,3,4,5,2,3,4,1]
print(l)


l.sort()
print(l)

l.pop()
print(l)

l.reverse()
print(l)

l1=l.copy()
print(l1)

l.extend(l1)
print(l)

l.append(10)
print(l)

print(l.count(10))

print(l.index(10))

l.insert(0,11)
print(l)

lnew=sorted(l)
print(lnew)

l.insert(0,'a')
print(l)

print(id(l))
print(id(l1))
l3=l1
print(l1)
print(l3)
print(id(l1))
print(id(l3))

l.remove(4)

print(l1)
print(l3)
print(id(l1))
print(id(l3))
l.remove(4)
print(l1)
print(l3)
print(id(l1))
print(id(l3))
list1=[1,2,3]
list2=list1
print(id(list1))
print(id(list2))
list1.remove(1)
print(id(list1))
print(id(list2))
print(list1)
print(list2)
listnew=[x**2 for x in range(5)]
print(listnew)

