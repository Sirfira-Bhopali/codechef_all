for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    z=li.count(0)
    t=li.count(2)
    sz=(z-1)*z/2
    st=(t-1)*t/2
    print(int(sz+st))