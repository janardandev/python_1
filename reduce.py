from functools import reduce

output=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(output)


output=reduce(lambda x,y:x*y,range(1,50))
print(output)