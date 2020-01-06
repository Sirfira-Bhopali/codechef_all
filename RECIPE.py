import math
for _ in range(int(input())):
    list1 = list(map(int, input().split()))
    j = math.gcd(list1[1],list1[2])
    if len(list1) > 3:
        z = 3
        for m in range(len(list1)-3):
            j = math.gcd(j, list1[z])
            z += 1
    list1.pop(0)
    list2 = []
    for i in list1:
        list2.append(int(i/j))
    '''for g in range(len(list2)):
        print(list2[g], end=" ")'''
    print(*list2)

