from functools import reduce

s=list(filter(lambda x:x%2==0,[1,2,3,4,5,6]))
print(s)


l=[1,2,3,4,5,6]
s=list(filter(lambda x:x%2==0,l))
print(s)

t=('a','aa','aaa','aaaa','aaaaa')
out=tuple(filter(lambda s:len(s)>3,t))
print(out)
