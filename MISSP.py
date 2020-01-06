#I'm using underscore cause it's faster than variable
for _ in range(int(input())):
    list1 = []
    #line 5 is for getting input of dolls
    for __ in range(int(input())):
        list1.append(input())
    #line 8 forms a dictionary so that repeated elements can be terminated and keys are stored in list
    list2 = list(dict.fromkeys(list1))
    for m in list2:
        #comparing every element of non-repeated list with 2
        if list1.count(m) != 2:
            print(m)
