a = int(input())
b = 0
c = 0
while a != 0:
    if a >= b:
        c = b
        b = a
    if c < a and a < b:
        c = a
    a = int(input())
print(c)