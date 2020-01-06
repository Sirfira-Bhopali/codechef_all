for _ in range(int(input())):
    num = input()
    a = num.count('0')
    b = num.count('1')
    if a == 1 or b == 1:
        print('Yes')
    else:
        print('No')

