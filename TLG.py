t = int(input())
list1 = []
for _ in range(t):
    score1, score2 = map(int, input().split())
    lead = score1 - score2
    list1.append(lead)
list1.sort()
if abs(list1[0]) > abs(list1[t-1]):
    w = 2
    print(w,(abs(list1[0])))
if abs(list1[t-1]) > abs(list1[0]):
    w = 1
    print(w,(abs(list1[t-1])))
