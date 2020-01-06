nu=0
de=0
for _ in range(int(input())):
    n,d=map(int,input().split("/"))
    nu=nu+n
    de=de+d
if nu>de:
    small=de
else:
    small=nu
for i in range(1,small+1):
    if ((nu%i==0) and (de%i==0)):
        gcd = i
print(str(int(nu/gcd))+"/"+str(int(de/gcd)))