def f(a,b):
    tb = [[0 for i in range(N // 2)] for j in range(N // 2)]
    r = 0
    for m in a:
        c = 0
        for n in b:
            if m == n:
                tb[r][c] = tb[r][c]+1
            if r > 0 and c > 0 and tb[r - 1][c - 1] != 0 and m==n:
                tb[r][c] = tb[r - 1][c - 1] + 1
            c += 1
        r += 1
    maximum=max(list(map(max, tb)))
    return maximum

for _ in range(int(input())):
    N=int(input())
    s=input()
    if N==1:
        print("0")
    if N%2==0:
        a=list(s[:N//2])
        b=list(s[N//2:])
        max4=f(a,b)
        mid=s[(N//2)-1:(N//2)+1]
        if max4<2 and mid in s[:(N//2)-1]:
            max4=2
        if max4<2 and mid in s[(N//2)+1:]:
            max4=2
        print(max4)

    #odd

    if N%2!=0 and N!=1:
        a=list(s[:int(N/2)])
        b=list(s[int(N/2)+1:])
        max1=f(a,b)

    #2

        a = list(s[:int(N/2)])
        b = list(s[int(N/2):N-1])
        max2=f(a,b)

    #3

        a = list(s[1:int(N/2)+1])
        b = list(s[int(N/2)+1:N])
        max3=f(a,b)
        print(max(max1,max2,max3))