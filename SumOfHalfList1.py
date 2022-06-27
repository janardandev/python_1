# list1=[x**2 for x in range(1,10)]
# print(list1)
# l1=[1,2,3,4,1,2,3]

def fun1(x):
    count=len(x)
    print(count)
    if count%2==0:
        middle=count//2
        firsthalf=x[:middle]
        secondhalf=x[middle:]
        sum1=sum(firsthalf)
        sum2=sum(secondhalf)
        if sum1==sum2:
            print("you are lucky")
        else:
            print("better luck next time")
    else:
        print("check your number again")
fun1((1,2,3,4,4,3,2,1,3,4))