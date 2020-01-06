l=int(input())
b=int(input())
a=l*b
p=2*(l+b)
if a>p:
    print('Area')
    print(a)
if p>a:
    print("Peri")
    print(p)
if a==p:
    print("Eq")
    print(a)