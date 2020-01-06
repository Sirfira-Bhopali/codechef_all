for _ in range(int(input())):
    N=int(input())
    s=input()
    if N%2==0:
        a=list(s[:N//2])
        b=list(s[N//2:])
        tb=[[0 for i in range(N//2)] for j in range(N//2)]
        print(a)
        print(b)
        r=0
        for m in a:
            c=0
            for n in b:
                if m==n:
                    tb[r][c]+=1
                if r>0 and c>0 and tb[r-1][c-1]!=0:
                    tb[r][c]=tb[r-1][c-1]+1
                c+=1
            r+=1
        max=max(list(map(max,tb)))
        mid=s[(N//2)-1:(N//2)+1]
        if max<2 and mid in s[:(N//2)-1]:
            max=2
        if max<2 and mid in s[(N//2)+1:]:
            max=2
        print(max)