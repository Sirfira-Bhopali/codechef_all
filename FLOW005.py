for _ in range(int(input())):
    price = int(input())
    count = 0
    while price > 0:
        list1 = [1,2,5,10,50,100]
        list1.append(price)
        list1.sort()
        x = list1.index(price)
        if price > 100:
            price = price - 100
        else:
            if price == list1[x+1]:
                price = 0
            if price != list1[x+1]:
                price = price - list1[x-1]
        count += 1
    print(count)