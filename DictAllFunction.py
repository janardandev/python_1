d={}
for i in range (5):
    d[i+1]=chr(65+i)
print(d)
d1={}
for i in range (5):
    d1[i+1]=chr(70+i)
print(d1)
d2={}
for i in range (5):
    d2[i+1]=chr(75+i)
print(d2)


# print(d1)
d.pop(1)
print(d)
dnew=d.copy()
print(dnew)
d.items()
for i in d.items():
    print(i)
print(d.keys())
for k in d.keys():
    print (k)
print(d.values())
for v in d.values():
    print(v)

d.popitem()
print(d)

print(d.get(3))
print(d.get(30))
print(d.get(30,'janardan'))
print(d.setdefault(6,'jd'))
print(d)
#print(d.fromkeys(6))
d.clear()
print(d)

d11={1:101,2:102}
d22={3:333,4:444}
d11.update(d22)
print(d11)
d333=d11.copy()
print(d333)
d234={**d11,**d22}
print("comprehension",d234)

d11=[11,22,33,44]
d22=[111,222,333,444]
new={x:y for x,y in zip(d11,d22)}
print(new)