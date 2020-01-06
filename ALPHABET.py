st = list(input())
for _ in range(int(input())):
    word = input()
    for x in word:
        if x not in st:
            print("No")
            break
    else:
        print("Yes")