for _ in range(int(input())):
    str1 = input()
    str2 = input()
    list1 = []
    list2 = []
    for s1 in str1:
        list1.append(s1)
    for s2 in str2:
        list2.append(s2)
    x = 0
    for m in range(len(list1)):
        if list1[x] != list2[x] and list1[x] != "?" and list2[x] != "?":
            print("No")
            break
        x += 1
    else:
        print("Yes")
    '''if x == len(list1):
        print("Yes")'''
