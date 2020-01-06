for _ in range(int(input())):
    c,d,l=map(int,input().split())
    dl=d*4
    cl=c*4
    if l in range((d-2*c)*4,dl+cl+1) and l%4==0:
        print('yes')
    else:
        print("no")