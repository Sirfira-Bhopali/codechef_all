test_cases = int(input())
while test_cases > 0:
    base = int(input())
    count = 0
    y = 0
    test_cases -= 1
    while (base-2) >= 2:
        num_squares = int((base - 2) / 2)
        if num_squares >= 2:
            y = 2 * num_squares - 1
        if num_squares < 2:
            y = num_squares
        count = count+y
        base=base-4
    print(count)