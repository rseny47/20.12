#Определи количество четных элементов в последовательности,
# завершающейся числом 0.Определи количество четных элементов в последовательности, завершающейся числом 0.
a = int(input())
b = 0
while a !=0:
    a = int(input())
    if a%2 == 0:
        b = b+1
print(b-1)