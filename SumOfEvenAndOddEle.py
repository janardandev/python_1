#sum of all even and all odd elements of a list
list1=[1,5,4,3,6,8,9]
length=len(list1)
print(length)
listodd=list1[0::2]
print(listodd)
listeven=list1[1::2]
print(listeven)
print(sum(listodd))
print(sum(listeven))