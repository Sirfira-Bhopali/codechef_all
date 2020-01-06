for _ in range(int(input())):
    s = list(map(int, input().split()))
    y = dict.fromkeys(s)
    for x in y:
        if s.count(x) != 2 and s.count(x) != 4:
            print("No")
            break
    else:
        print("Yes")