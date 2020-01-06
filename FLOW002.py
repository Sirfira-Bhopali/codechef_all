test_cases = int(input())
for test_cases in range(test_cases):
    num1, num2 = map(int, input().split())
    print(num1 % num2)
