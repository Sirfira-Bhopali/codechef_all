for _ in range(int(input())):
    list1 = []
    j, k, l = map(int, input().split())
    list1.append(j)
    list1.append(k)
    list1.append(l)
    list1.sort()
    print(list1[1])
