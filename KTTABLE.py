for _ in range(int(input())):
    stud = int(input())
    time_assigned = list(map(int, input().split()))
    time_taken = list(map(int, input().split()))
    time_assigned.append(0)
    time_assigned.sort()
    x = 0
    count = 0
    for _ in range(stud):
        time = time_assigned[x + 1] - time_assigned[x]
        if time >= time_taken[x]:
            count += 1
        x += 1
    print(count)