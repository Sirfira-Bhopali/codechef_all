for _ in range(int(input())):
    num = int(input())
    f = 1
    while num>1:
        f = f*num
        num -= 1
    print(f)