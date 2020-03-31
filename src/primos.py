# programa python com os numeros primos


def ehprimo(primo):
    for x in range(2, primo+1):
        if x != primo:
            x = primo % x
            if x == 0:
                return False
        else:
            return True

cont = 0
num = 2
while cont <= 100:
    if ehprimo(num) is True:
        print(num)
        cont += 1
    num = num + 1
print("Tem:",cont)


