test_cases = int(input())
i=0
dict1 = {}
score=0
while test_cases > 0:
    for i in range(0,2):
        str = input()
        li = list(str.split(" "))
        i += 1

        if not li[0] in dict1.keys() and li[1] > li[3]:
            dict1.update({li[0]: score+1})
        if li[0] in dict1.keys() and li[1] > li[3]:
            dict1[li[0]]=score+1
        if not li[4] in dict1.keys() and li[3] > li[1]:
            dict1={li[4]: score+1}
        if li[4] in dict1.keys() and li[3] > li[1]:
            dict1[li[4]]=score+1
    print(dict1)
    test_cases -= 1
