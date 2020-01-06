test_cases = int(input())
while test_cases > 0:
    str1 = input()
    str2 = input()
    minimum = 0
    maximum = 0
    x = 0
    for letters in str1:
        if str1[x] == "?" and str2[x] == "?":
            maximum = maximum + 1
        if str1[x] != str2[x] and str1[x] != "?" and str2[x] != "?":
            minimum = minimum + 1
            maximum = maximum + 1
        if str1[x] == "?" and str2[x] != "?":
            maximum = maximum + 1
        if str1[x] != "?" and str2[x] == "?":
            maximum = maximum + 1
        x += 1

    print(str(minimum)+" "+str(maximum))
    test_cases -= 1
