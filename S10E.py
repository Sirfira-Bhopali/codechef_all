for _ in range(int(input())):
    len=int(input())
    prices = list(map(int, input().split()))
    l=0
    c=0
    for _ in prices:
        if l<5:
            blabla= prices[:l + 1]
        else:
            blabla= prices[l - 5:l + 1]
        if min(blabla)==blabla[-1] and blabla.count(min(blabla))==1:
            c+=1
        l += 1
    print(c)
