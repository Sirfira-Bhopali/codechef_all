test_cases = int(input())
for test_cases in range(test_cases):
    num = int(input())
    sum = 0
    for integer in str(num):
        sum = sum+int(integer)
    print(sum)