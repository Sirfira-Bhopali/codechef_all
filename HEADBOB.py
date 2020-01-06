for _ in range(int(input())):
    x = int(input())
    string = input()
    if "I" in string:
        print("INDIAN")
    if not "I" in string and not "Y" in string and "N" in string:
        print("NOT SURE")
    if not "I" in string and "Y" in string:
        print("NOT INDIAN")