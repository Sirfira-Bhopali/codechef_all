test_cases = int(input())
list1=[]
for test_cases in range (test_cases):
    list1.append(int(input()))
list1.sort()
for numbers in list1:
    print(numbers)