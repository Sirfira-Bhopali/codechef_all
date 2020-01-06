test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    x=1
    while num > 1:
        x = x*num
        num -= 1
    print(x)
