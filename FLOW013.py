for _ in range (int(input())):
    ang1, ang2, ang3 = map(int,input().split())
    if ang1 + ang2 + ang3 == 180:
        print("YES")
    else:
        print("NO")