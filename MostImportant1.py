set1={1,2,3,4,5}
set2={3,4,5,6}
set3={*set1,*set2}
print(type(set3))
print(set3)

s1={1,2,3}
t1=(1,4,5)
l1=[7,8,9]
final=(*s1,*t1,*l1)
print(type(final))
print(final)

l3=(7,8,9)
l4=[10,11,12]
final=[*l3,*l4]
print(final)
print(type(final))

t3=(7,8,9)
t4=(10,11,12)
final=(*t3,*t4)
print(final)
print(type(final))