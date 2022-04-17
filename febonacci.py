
import time
def febn():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=febn()
for x in g:
    if x >100:
        break
    print (x)
    time.sleep(1)
