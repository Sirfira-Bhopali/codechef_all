t = int(input())
for _ in range(t):
    list1 = []
    num1 = int(input())
    for integer in str(num1):
        list1.append(integer)
    print(int(list1[0])+int(list1[len(str(num1))-1]))
