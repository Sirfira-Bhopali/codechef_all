for _ in range(int(input())):
    num = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    lr = []
    ind = []
    ind2 = []
    j = 0
    for __ in range(num):
        lr.append(l[j]*r[j])
        j += 1
    count = 0
    for x in lr:
        if x == max(lr):
            ind.append(count)
        count += 1
    if len(ind) > 1:
        for y in ind:
            if r[y] == max(r):
                ind2.append(y)
    if len(ind) == 1:
        print(ind[0]+1)
    if len(ind2) > 1:
        print(min(ind2)+1)
    if len(ind2) == 1:
        print(ind2[0]+1)