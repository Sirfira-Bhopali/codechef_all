test_cases=int(input())
while test_cases>0:
    num=int(input())
    test_cases-=1
    count=0
    for integer in str(num):
        if integer=="4":
            count+=1
    print(count)