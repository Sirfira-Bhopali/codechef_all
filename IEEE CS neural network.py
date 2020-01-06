n=int(input())
l1=list(map(int,input().split()))
l1.sort()
k=int(input())
l2=list(map(int,input().split()))
for x in l2:
    count=0
    for y in l1:
        if x>y:
            l1[count]=x+1
        count+=1
print(l1)
