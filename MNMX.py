for _ in range(int(input())):
    size = int(input())
    list1 = list(map(int, input().split()))
    print(min(list1)*(size-1))