for _ in range(int(input())):
    num = int(input())
    string = str(num)
    string = string[::-1]
    if string == str(num):
        print("wins")
    else:
        print("losses")