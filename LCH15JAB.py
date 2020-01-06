for _ in range(int(input())):
    s = input()
    list1 = list(dict.fromkeys(s))
    list2 = []
    for mn in list1:
        list2.append(s.count(mn))
    l = max(list2)
    if l == len(s)/2:
        print("YES")
    else:
        print("NO")