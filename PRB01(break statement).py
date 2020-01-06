for _ in range(int(input())):
    num = int(input())
    if num == 1 or num == 2:
        print("yes")
    if num%2 == 0 and num != 2:
        print("no")
    if num%2 != 0:
        m = 1
        while m < int(num/2):
            m += 2
            if num%m == 0:
                print("no")
                break
        else:
            print("yes")





