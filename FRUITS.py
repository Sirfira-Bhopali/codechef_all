for _ in range(int(input())):
    apple, orange, gold = map(int, input().split())
    if apple > orange:
        diff = apple - orange
        if gold >= diff:
            print(0)
        else:
            print(apple - orange - gold)
    if apple < orange:
        diff = orange - apple
        if gold >= diff:
            print(0)
        else:
            print (orange - apple - gold)
    if apple == orange:
        print(0)