t=int(input())
while(t>0):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    t-= 1
    if num1 > num2:
        print(">")
    if num1 < num2:
        print("<")
    if num1 == num2:
        print("=")