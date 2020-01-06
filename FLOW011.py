for _ in range (int(input())):
    salary = int(input())
    if salary < 1500:
        GS = salary + (0.1 * salary) + (0.9 * salary)
    if salary >= 1500:
        GS = salary + 500 + (0.98*salary)
    print(GS)