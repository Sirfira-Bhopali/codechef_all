for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if n%2==0:
        if a>=b:
            print(a//b)
        if b>a:
            print(b//a)
    else:
        if 2*a>=b:
            print(2*a//b)
        if 2*a<b:
            print(b//2*a)
