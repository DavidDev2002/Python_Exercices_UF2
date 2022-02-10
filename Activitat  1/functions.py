def validate():
    num = int(input("Introduce un número natural: "))
    while num < 1:
        num = int(input("Introduce un número natural: "))
    return num

def binary(num):
    count = 1
    binario = 0
    while num != 0:
        rem = num % 2
        num = num // 2
        binario = binario + (rem * count)
        count = count * 10
    return binario

def validar():
    error = "Has introdicido 3 veces valores erroneos"
    num = print(int(input("Introduce un numero entre 10 y 5000: ")))
    i = 0
    while num > 1 and num < 5000:
        num = int(input("Introduce un numero entre 10 y 5000: "))
        i += 1
        if i > 3:
            return error
        else:
            return num


