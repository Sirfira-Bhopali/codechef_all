for _ in range(int(input())):
    a,b = map(int,input().split())
    x = 1
    list0=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
    list1=[0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600, 650, 702, 756, 812, 870, 930, 992]
    for _ in list0:
        if _>a and a<961:
            n=list0.index(list0[list0.index(_)-1])
            break
        if a>=961:
            n=31
    for __ in list1:
        if __>b and b<992:
            m = list1.index(list1[list1.index(__) - 1])
            break
        if b>=992:
            m=31
    if n>m:
        print("Limak")
    if n<=m:
        print('Bob')





