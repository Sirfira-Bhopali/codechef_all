import math
for _ in range(int(input())):
    n=int(input())
    count=0
    while n%10==0:
        count+=1
        n=n//10
    k=math.log(n,2)
    if k.is_integer() and count>=k:
        print('Yes')
    else:
        print('No')