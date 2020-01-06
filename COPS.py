for _ in range(int(input())):
    m, x, y = map(int, input().split())
    houses = list(map(int, input().split()))
    j = x * y
    list2 = []
    for house in houses:
        if house - j <= 0 and house + j < 101:
            for el in range(1, house+j+1):
                list2.append(el)
        if house - j > 0 and house + j < 100:
            for ele in range(house -j, house+j+1):
                list2.append(ele)
        if house - j > 0 and house + j >= 100:
            for elem in range(house-j, 101):
                list2.append(elem)
        if house - j <= 0 and house + j > 100:
            for element in range(1, 101):
                list2.append(element)
    list3 = list(dict.fromkeys(list2))
    print(100-len(list3))