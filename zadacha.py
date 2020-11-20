import random
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zamen = 4
strochka = input("Введите строчку")
a = 0
b = 3
for i in strochka:
    for i in range(b):
        if a == 1 :
            print(random.choice(list), end='')
            a += 1
        elif a == zamen:
            print(random.choice(list), end='')
            a += 1
            zamen += 3
        else:
            print(strochka[a], end='')
            a += 1
    print("")
    