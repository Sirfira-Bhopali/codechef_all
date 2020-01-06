test_cases = int(input())
while test_cases > 0:
    no_cmd, pos = map(int,input().split())
    cmd=input()
    l_count = 0
    r_count = 0
    for each_cmd in cmd:
        if each_cmd == "R":
            r_count += 1
        if each_cmd == "L":
            l_count += 1
    if l_count>r_count:
        print(no_cmd-r_count+1)
    if r_count>l_count:
        print(no_cmd-l_count+1)
    test_cases -= 1