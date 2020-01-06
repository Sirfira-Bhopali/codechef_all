test_cases, divisor=input().split()
test_cases=int(test_cases)
divisor=int(divisor)
count=0
while test_cases>0:
    num = int(input())
    if num%divisor == 0:
        count += 1
    test_cases -= 1
print(count)