for _ in range(int(input())):
    n, m = map(int, input().split())
    if n > m:
        print(n, n+m)
    else:
        print(m, n+m)