for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=max(l)
    b=min(l)
    m=l.index(a)
    n=l.index(b)
    if m>n:
        print(b,a)
    if n>m:
        print(a,b)