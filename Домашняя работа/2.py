a=int(input())
b=a
c=1
while a!=0:
    a=int(input())
    if a>b:
        b=a
        c=1
    elif a==b:
        c= c+1
print(c)