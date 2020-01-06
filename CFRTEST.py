for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    x = -1
    count = 0
    for y in range(len(d)-1):
        x += 1
        if d[x] == d[x+1]:
            count += 1
    print(n-count)