word=input()
list1=[]
list2=[]
for _ in word:
    if _ != " ":
        print("_",end="")
        list1.append("_")
    if _ == " ":
        print(" ", end="")
        list1.append(" ")
for w in word:
    list2.append(w)
tries=0
while tries<5:
    guess = input()
    if guess not in list2:
        tries+=1
    a=0
    for __ in word:
        if guess == __:
            list1[a]=guess
        a+=1
    print(*list1)
    if list1== list2:
        print("you won")



