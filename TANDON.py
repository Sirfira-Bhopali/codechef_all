for _ in range(int(input())):
    N,K=map(int,input().split())
    b=[]
    for __ in range(10**N):
        if __%K==0:
            b.append(__)
    c=[]
    for ___ in b:
        z=int(str(___)[::-1])
        if z in b:
            c.append(___)
    print(len(c))


