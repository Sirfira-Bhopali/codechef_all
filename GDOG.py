for _ in range(int(input())):
    coins, person = map(int, input().split())
    m = 1
    list1 = []
    for i in range(person):
        j = coins % m
        list1.append(j)
        m += 1
    print(max(list1))