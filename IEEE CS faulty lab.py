for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    for x in l1:
        if x not in l2:
            l2.append(x)
    if n==len(l2):
        print("FAULTY")
    if n!=len(l2):
        print("NOT FAULTY")