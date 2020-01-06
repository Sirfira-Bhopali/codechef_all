for _ in range(int(input())):
    n = int(input())
    c = input()
    list1 = []
    r = c.count("R")
    g = c.count("G")
    b = c.count("B")
    list1.append(r)
    list1.append(g)
    list1.append(b)
    print(n-max(list1))
