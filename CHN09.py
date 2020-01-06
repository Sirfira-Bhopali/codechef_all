for _ in range(int(input())):
    s = input()
    a = s.count('a')
    b = s.count('b')
    if a > b:
        print(b)
    if a < b:
        print(a)
    if a == b:
        print(a)