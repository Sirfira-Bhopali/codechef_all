import math
t= int(input())
count=1
while count<=t:
    num_circle=int(input())
    count+=1
    remaining_circle=num_circle
    count1=1
    while remaining_circle>0:
        side=int(math.sqrt(num_circle))
        remaining_circle=num_circle-(side*side)
        side=int(math.sqrt(remaining_circle))
        num_circle = remaining_circle
        count1+=1
    print(count1-1)



