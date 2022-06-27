s=lambda x,y:x+y
print(s(2,3))

s=lambda x:x**2
print(s(8))

s=lambda x,y,z:x+y+z
print(s(2,3,4))
s=lambda x,y,z,a,b,c:x+y+z+a+b+c
print(s(1,2,3,4,5,6))
s=lambda a,b:a if a>b else b
print(s(40,20))
s=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(s(70,50,30))