for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    for x in l1:
        if l1.count(x)%2!=0:
            print(x)