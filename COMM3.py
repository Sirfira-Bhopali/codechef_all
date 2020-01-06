import math
for _ in range(int(input())):
    dist = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list3 = list(map(int, input().split()))
    list4 = list1 + list2 + list3
    dist12 = math.sqrt((list4[0] - list4[2]) ** 2 + (list4[1] - list4[3]) ** 2)
    dist23 = math.sqrt((list4[2] - list4[4]) ** 2 + (list4[3] - list4[5]) ** 2)
    dist31 = math.sqrt((list4[0] - list4[4]) ** 2 + (list4[1] - list4[5]) ** 2)
    if dist12 <= dist and dist23 <= dist and dist31 > dist:
        print('yes')
    elif dist31 <= dist and dist23 <= dist and dist12 > dist:
        print('yes')
    elif dist12 <= dist and dist31 <= dist and dist23 > dist:
        print('yes')
    elif dist12 <= dist and dist31 <= dist and dist23 <= dist:
        print('yes')
    else:
        print('no')