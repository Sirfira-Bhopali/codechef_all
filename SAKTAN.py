import numpy as np
for _ in range(int(input())):
    n,m,q=map(int,input().split())
    k=np.zeros([n,m],dtype=int)
    for __ in range(q):
        x,y=map(int,input().split())
        k[x-1,:]+=1
        k[:,y-1]+=1
k=k.flatten()
c=0
for ___ in k:
    if ___%2!=0:
        c+=1
print(c)