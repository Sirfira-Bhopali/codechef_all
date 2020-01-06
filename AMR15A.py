t = int(input())
weapons = list(map(int, input().split()))
count = 0
for m in weapons:
    if m%2 == 0:
        count = count + 1
if count >= (int(t/2) + 1):
    print('READY FOR BATTLE')
else:
     print("NOT READY")