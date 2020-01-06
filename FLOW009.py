for _ in range(int(input())):
    qty, price = map(float, input().split(' '))
    if qty > 1000:
        print("%.6f" % (0.9*(qty*price)))
    else:
        print("%.6f" % (qty*price))