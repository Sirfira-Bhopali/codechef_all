for _ in range(int(input())):
    n=int(input())
    c=0
    while n%10==0:
        n=n%10
        c=c+1
    print(n,c)