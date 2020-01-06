for _ in range(int(input())):
    n,m,q=map(int,input().split())
    list1=[0]*n*m
    for __ in range(q):
        x,y=map(int,input().split())
        for ___ in range((x-1)*m,x*m):
            list1[___]+=1
        for k in range(y-1,m*n,m):
            list1[k]+=1
c=0
for m in list1:
    if m%2!=0:
        c+=1
print(c)