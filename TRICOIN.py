for _ in range(int(input())):
    n = int(input())
    x = 1
    while n >= x:
        n = n - x
        x += 1
    print(x-1)