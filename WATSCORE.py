for _ in range(int(input())):
    l1=[0]
    l2=[0]
    l3=[0]
    l4=[0]
    l5=[0]
    l6=[0]
    l7=[0]
    l8=[0]
    for __ in range(int(input())):
        m,n=map(int,input().split())
        if m==1:
            l1.append(n)
        if m==2:
            l2.append(n)
        if m==3:
            l3.append(n)
        if m==4:
            l4.append(n)
        if m==5:
            l5.append(n)
        if m==6:
            l6.append(n)
        if m==7:
            l7.append(n)
        if m==8:
            l8.append(n)
    print(max(l1)+max(l2)+max(l3)+max(l4)+max(l5)+max(l6)+max(l7)+max(l8))
