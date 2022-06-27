d1={'A':1,'B':2,'C':3}
d2={'D':4,'E':5,'F':6}
d3={**d1,**d2}
print(type(d3))
print(d3)
d4={*d1,*d2}
print(d4)
print(type(d4))

d5=[*d1.keys(),*d2.keys()]
print(d5)

d5=[*d1.values(),*d2.values()]
print(d5)
d6=print({*d1})

# r=range(5)
# print(list(r))
# l=list(range(5))
# print(l)
